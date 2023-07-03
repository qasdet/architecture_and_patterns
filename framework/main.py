from quopri import decodestring
from framework.frame_requests import GetRequests, PostRequests


class PageNotFound:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class Framework:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ: dict, start_response):
        path: str = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        request = {}

        # Получаем все данные запроса
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = Framework.decode_value(data)
            print(f'Нам пришёл post-запрос: {Framework.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = Framework.decode_value(request_params)
            print(f'Нам пришли GET-параметры: {Framework.decode_value(request_params)}')

        view = self.routes.get(path, PageNotFound())

        for i in self.fronts:
            i(request)

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')

            key = bytes(k.replace('%', '=').replace("+", " "), 'UTF-8')
            key_decode_str = decodestring(key).decode('UTF-8')

            new_data[key_decode_str] = val_decode_str
        return new_data
