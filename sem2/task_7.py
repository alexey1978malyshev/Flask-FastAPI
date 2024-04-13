"""📌 Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
📌 При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат"""

from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def pow_num():
    if request.method == 'POST':
        num = int(request.form.get('number'))
        return f'Квадрат числа {num} = {num**2}'
    return render_template('form_pow.html')


if __name__ == '__main__':
    app.run(debug=True)