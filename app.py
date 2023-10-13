from app import app
from app.users import user
from app.projects import project
from app.interfacecase import interfacecase

app.register_blueprint(user)
app.register_blueprint(project)
app.register_blueprint(interfacecase)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
