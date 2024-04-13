"""📌 Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
📌 При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста"""

from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        if int(request.form.get('age')) >= 18:
            return "Вы вошли"
        return 'Возраст слишком мал'
    return render_template('form_name_age.html')


if __name__ == '__main__':
    app.run(debug=True)