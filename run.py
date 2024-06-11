from gevent import monkey

monkey.patch_all(thread=False, select=False)

from app import app
from app.users import user
from app.projects import project
from app.interfacecase import interfacecase
from app.tools import tools
from app.tasks import tasks
from gevent.pywsgi import WSGIServer

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(project, url_prefix='/project')
app.register_blueprint(interfacecase, url_prefix='/interfacecase')
app.register_blueprint(tools, url_prefix='/tools')
app.register_blueprint(tasks, url_prefix='/tasks')



@app.route('/')
def hello_world():
    return 'Hello World!'


def app_start():
    http_server = WSGIServer(('0.0.0.0', 3000), app)
    http_server.serve_forever()


if __name__ == '__main__':
    app_start()
