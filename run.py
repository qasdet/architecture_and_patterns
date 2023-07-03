from wsgiref.simple_server import make_server
from framework.main import Framework
import views
from patterns.structural_patterns import routes
from urls import fronts


application = Framework(routes, fronts)

with make_server('', 8080, application) as httpd:
    print('Serving on port 8000...')
    httpd.serve_forever()
