"""📌 Дорабатываем задачу 1.
📌 Добавьте две дополнительные страницы в ваше веб-
приложение:
○ страницу "about"
○ страницу "contact"."""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world!'


@app.route('/about/')
def about():
    return f'<h1>Обо мне!</h1>'


@app.route('/contact/')
def contact():
    return 'Мои контакты:'


if __name__ == '__main__':
    app.run(debug=True)
