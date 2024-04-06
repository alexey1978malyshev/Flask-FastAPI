"""📌 Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
📌 Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
📌 Данные о студентах должны быть переданы в шаблон через
контекст"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    _students = [
        {'first_name' :'Алексей',
         'last_name': 'Петров',
         'age': '25',
         'grade': '8',
         },
        {'first_name': 'Сергей',
         'last_name': 'Иванов',
         'age': '18',
         'grade': '6',
         },
        {'first_name': 'Иван',
         'last_name': 'Кузнецов',
         'age': '21',
         'grade': '4',
         },
    ]
    context = {'students': _students}

    return render_template('students_info.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
