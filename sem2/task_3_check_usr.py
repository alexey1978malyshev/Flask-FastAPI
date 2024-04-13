"""📌 Создать страницу, на которой будет форма для ввода логина
и пароля
📌 При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой."""

from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def check_usr():
    login = 'Alex'
    password = 'qwe'

    if request.method == 'POST':
        if not request.form['login']:
            return render_template('form_login_pass.html')

        if request.form.get('login')  == login and request.form.get('password') == password:

            return render_template('main.html')
        else:
            return render_template('err_usr.html')

    return render_template('form_login_pass.html')


if __name__ == '__main__':
    app.run(debug=True)
