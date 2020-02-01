from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'RANDOMSTRING'
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.add_extension('jinja2.ext.do')

    db.init_app(app)
    login_manager.init_app(app)
    csrf = CSRFProtect(app)

    from pod.users.routes import users
    from pod.picks.routes import picks
    app.register_blueprint(users)
    app.register_blueprint(picks)

    return app
