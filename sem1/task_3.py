"""📌 Написать функцию, которая будет принимать на вход два
числа и выводить на экран их сумму.

📌 Написать функцию, которая будет принимать на вход строку и
выводить на экран ее длину."""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет!'


@app.route('/<int:a>/<int:b>/')
def summa(a, b):
    return str(a + b)

@app.route('/<string:s>/')
def str_len(s):
    return f'Длина строки = {len(s)}'


if __name__ == '__main__':
    app.run(debug=True)
