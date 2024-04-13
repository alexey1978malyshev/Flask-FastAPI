"""📌 Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени."""

from flask import Flask,render_template

app = Flask(__name__)


@app.get('/')
def index_get():
    return render_template('putme.html')


@app.post('/form')
def index_post():
    return render_template('base.html')




if __name__ == '__main__':
    app.run(debug=True)