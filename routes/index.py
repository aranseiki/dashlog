from flask import Flask, render_template
from py_rpautom.python_utils import abrir_arquivo_texto


def index(app: Flask):
    @app.route('/')
    def _():
        return route_content()


def route_content():
    file_content = abrir_arquivo_texto(
        caminho=r'C:\dev\projects\dashlog\data\input\Processes.csv',
        encoding='utf8',
    ).splitlines()

    file_content_temp = [line.split(';') for line in file_content]

    file_content_temp_2 = []
    for line in file_content_temp:
        file_content_temp_2.append(
            [collumn.replace('"', '') for collumn in line]
        )

    file_content = file_content_temp_2

    return render_template('index.html', data=file_content)
