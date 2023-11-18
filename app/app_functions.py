from flask import Flask
from routes import index


def application(debug: bool = True):
    app = Flask(import_name=__name__)
    app.debug = debug

    index.index(app=app)

    return app
