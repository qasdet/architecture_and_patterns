from urls import routes
from framework.main import Framework
from wsgiref.simple_server import make_server

app = Framework(routes)


with make_server('', 8080, app) as httpd:
    print("Запуск на порту 8080...")
    httpd.serve_forever()