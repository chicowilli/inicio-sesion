import os

from flask import Flask
from dotenv import load_dotenv

from flask_app.controllers.usuarios import usuarios


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY")

    if not app.config["SECRET_KEY"]:
        raise RuntimeError("Configura la variable de entorno FLASK_SECRET_KEY.")

    app.register_blueprint(usuarios)
    return app
