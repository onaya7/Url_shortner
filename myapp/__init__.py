from flask import Flask
from myapp.views import view 
from myapp.models import db


def create_app(config_file='config.py'):
        
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.register_blueprint(view)

    db.init_app(app)
    

    return app


