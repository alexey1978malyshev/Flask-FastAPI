from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from pathlib import PurePath, Path

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')

import os

# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST': # если получен POST запрос(отправка данных на сервер)
#         file = request.files.get('file') # сохраняем файл из запроса в переменную file
#         file_name = secure_filename(file.filename) # получаем безопасное имя файла
#         upload_dir = PurePath.joinpath(Path.cwd(), 'uploads') # путь к директории загрузки
#         if not os.path.exists(upload_dir): # проверяем, существует ли директория
#             os.makedirs(upload_dir) # если нет, создаем её
#         file.save(PurePath.joinpath(upload_dir, file_name)) # сохраняем файл на сервере
#         return f"Файл {file_name} загружен на сервер" # возвращаем сообщение о загрузке файла
#     return render_template('upload.html') # если метод запроса GET, то возвращаем шаблон формы для загрузки файла


if __name__ == '__main__':
    app.run(debug=True)
