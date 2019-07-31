from website import db, app
from flask_script import Manager, Server
from website.models import Post
# from website.models 

manager = Manager(app)

manager.add_command("runserver", Server(port=5000, host='127.0.0.1'))
manager.add_command("debug", Server(use_debugger=True, use_reloader=True, port=5000, host='127.0.0.1'))

if __name__ == '__main__':
    manager.run()