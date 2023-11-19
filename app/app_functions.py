from flask import Flask
from py_rpautom import python_utils as pyutils
from routes import index


def application(debug: bool = True):
    project_path = pyutils.coletar_arvore_caminho(caminho=__name__)
    templates_path = '\\'.join((project_path, 'templates'))

    app = Flask(import_name=__name__)
    app.debug = debug
    app.template_folder = templates_path

    index.index(app=app)

    return app
