"""📌 Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
📌 При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!"."""

from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = '961617f2ec1eb1e84747c00822992a77bfe1c3f9325d516a8403038d1fc11dd6'


@app.route('/', methods=['GET', 'POST'])
def greeting():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('greeting'))
        # Обработка данных формы
        name = request.form.get('name')
        flash(f'Приветствую, {name}!', 'success')
        return redirect(url_for('greeting'))
    return render_template('students.html')


if __name__ == '__main__':
    app.run(debug=True)
