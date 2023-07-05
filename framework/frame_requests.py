class GetRequests:

    @staticmethod
    def parse_input_data(data: str):
        if data:
            return {item.split('=')[0]: item.split('=')[1] for item in data.split('&')}

        return dict()

    @staticmethod
    def get_request_params(environ):
        return GetRequests.parse_input_data(environ['QUERY_STRING'])


class PostRequests:

    @staticmethod
    def parse_input_data(data: str):
        if data:
            return {item.split('=')[0]: item.split('=')[1] for item in data.split('&')}
        return dict()


    @staticmethod
    def get_wsgi_input_data(env) -> bytes:
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0

        return env['wsgi.input'].read(content_length) if content_length > 0 else b''

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            # декодируем данные
            data_str = data.decode(encoding='utf-8')
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        data = self.get_wsgi_input_data(environ)

        return self.parse_wsgi_input_data(data)

