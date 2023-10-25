from gevent import monkey
monkey.patch_all(thread=False, select=False)

from app import app
from app.users import user
from app.projects import project
from app.interfacecase import interfacecase
from gevent.pywsgi import WSGIServer

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(project, url_prefix='/project')
app.register_blueprint(interfacecase, url_prefix='/interfacecase')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.debug = True
    server = WSGIServer(('127.0.0.1', 5000), app)
    server.serve_forever()
