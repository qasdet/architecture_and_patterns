from wsgiref.simple_server import make_server
from framework.main import Framework
import views
from patterns.structural_patterns import routes
from urls import fronts
from create_db import create_db


application = Framework(routes, fronts)
create_db()

with make_server('', 8080, application) as httpd:
    print('Serving on port 8000...')
    httpd.serve_forever()
