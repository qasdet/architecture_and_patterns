from wsgiref.simple_server import make_server
from framework.main import Framework
from framework.common import *
import views
from patterns.structural_patterns import routes
from urls import fronts
from create_db import create_db


def run_server(adr, port):
    application = Framework(routes, fronts)
    create_db()

    with make_server(adr, port, application) as httpd:
        print(f'Serving on port {port}...')
        httpd.serve_forever()


if __name__ == "__main__":
    run_server(DEFAULT_ADDRESS, DEFAULT_PORT)
