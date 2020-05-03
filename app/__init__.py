from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

bootstrap = bootstrap()
db = SQLAlchemy

def create_app(config_name):
    app = Flask(__name__)

    #initialize flask extensions
    bootstrap.init_app(app)
    db.init_app(app) 