"""📌 Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
📌 При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом"""


from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        first = int(request.form.get('first_num'))
        second = int(request.form.get('second_num'))
        operation = request.form.get('operation')
        result = 0
        match operation:
            case '+':
                result = first + second
            case '-':
                result = first - second
            case '*':
                result = first * second
            case '/':
                result = first / second
            case _:
                result = 'Неверная операция'



        return f'Результат вычисления: {first}{operation}{second} = {result}'
    return render_template('form_calc.html')


if __name__ == '__main__':
    app.run(debug=True)