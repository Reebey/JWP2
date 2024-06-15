from flask import Flask
from .forms import TaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from .config import config
from os import getenv


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # load config
    config_name = getenv('FLASK_CONFIG') or 'testing'
    app = Flask(__name__,
        static_url_path='',
        static_folder='web/static',
        template_folder='web/templates')
    app.config.from_object(config[config_name])
    Migrate(app, db)
    
    db.init_app(app)
    login_manager.init_app(app)
    
    from .auth import auth
    app.register_blueprint(auth)

    from .task import task
    app.register_blueprint(task)

    from .profile import profile
    app.register_blueprint(profile)

    from .main import main
    app.register_blueprint(main)
    
    return app
