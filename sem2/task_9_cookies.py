"""📌 Создать страницу, на которой будет форма для ввода имени
и электронной почты
📌 При отправке которой будет создан cookie файл с данными
пользователя
📌 Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
📌 На странице приветствия должна быть кнопка "Выйти"
📌 При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""
from flask import Flask, request, render_template, flash, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = '961617f2ec1eb1e84747c00822992a77bfe1c3f9325d516a8403038d1fc11dd6'


@app.route('/', methods=['GET', 'POST'])
def set_cookies():
    if request.method == 'POST':
        name = request.form.get('name')
        mail = request.form.get('mail')
        context = {
            'title': 'Приветствие',
            'name': name}
        print(name)
        if not name or not mail:
            flash('Введите имя и почту!', 'danger')
            return redirect(url_for('set_cookies'))
        # устанавливаем cookie
        response = make_response(render_template('main.html', **context))
        response.set_cookie('username', name)


        return response
    return render_template('students.html')

@app.route('/del_cookies', methods=['GET', 'POST'])
def del_cookies():
    if request.method == 'POST':
        response = make_response(render_template('students.html'))
        response.delete_cookie('username')
        return response
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
