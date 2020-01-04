from flask import Flask
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
  app.jinja_env.trim_blocks = True
  app.jinja_env.lstrip_blocks = True

  db.init_app(app)
  login_manager.init_app(app)

  from pod.users.routes import users
  from pod.picks.routes import picks
  # from pod.main.routes import main
  app.register_blueprint(users)
  app.register_blueprint(picks)
 # app.register_blueprint(main)

  return app
