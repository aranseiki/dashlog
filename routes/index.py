from flask import Flask
from py_rpautom.python_utils import abrir_arquivo_texto

def index(app: Flask):
    @app.route('/')
    def route():
        return route_content()

    return route()


def route_content():
    file_content = abrir_arquivo_texto(
        caminho=r'C:\dev\projects\dashlog\data\input\Processes.csv',
        encoding='utf8',
    ).splitlines()

    return file_content
