from flask import Flask
from .wordclouds.routes import clouds



def create_app():
    app = Flask(__name__)
    with app.app_context():
        app.register_blueprint(clouds, url_prefix="/word-clouds")
    return app 