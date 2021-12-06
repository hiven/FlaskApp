import os
from config import Config
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)

    from app.main import main_blueprint

    app.register_blueprint(main_blueprint)

    return app