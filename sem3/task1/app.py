"""📌 Создать базу данных для хранения информации о студентах университета.
📌 База данных должна содержать две таблицы: "Студенты" и "Факультеты".
📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
возраст, пол, группа и id факультета.
📌 В таблице "Факультеты" должны быть следующие поля: id и название
факультета.
📌 Необходимо создать связь между таблицами "Студенты" и "Факультеты".
📌 Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их факультета.
"""
from flask import Flask, render_template, jsonify
from models import db, Student, Faculty
from random import randint
from faker import Faker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentsdb.db'

db.init_app(app)
fake = Faker()


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_tables():
    count = 12

    # Добавляем факультеты

    for f in range(1, count // 3):
        new_faculty = Faculty(faculty_name=f'Faculty_{f}')
        db.session.add(new_faculty)
    db.session.commit()

    # Добавляем студентов
    for user in range(1, count + 1):
        gdr = 'male' if user % 2 == 0 else 'female'
        grp = 'day' if user % 3 == 0 else 'evening'
        faculty = randint(1, 3)
        # new_std = Student(first_name=f'student_{user}', last_name=f'student_{user}', age=randint(18, 30), gender=gdr, group=grp, id_faculty=faculty)
        new_std = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=fake.random_int(min=18, max=30),
            gender=fake.random_element(elements=("male", "female")),
            group=fake.random_int(min=100, max=999),
            id_faculty=faculty

        )

        db.session.add(new_std)
    db.session.commit()


@app.route('/students/')
def get_std():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

    """Faker - это библиотека для генерации случайных данных на различных языках программирования.
В Python она позволяет создавать фиктивные данные, такие как имена, адреса, электронные почты, числа телефонов, тексты и многое другое.

pip install faker
from faker import Faker
fake = Faker()

Создаем студента из первой семинарской задачи

new_student = Student(
                name=fake.first_name(),
                last_name=fake.last_name(),
                age=fake.random_int(min=18, max=30),
                gender=fake.random_element(elements=("male", "female")),
                group=fake.random_int(min=100, max=999),
                faculty_id=faculty_id
            )

Вы можете использовать Faker для создания различных типов данных в вашем приложении.
Он полезен для написания тестов, заполнения баз данных тестовыми данными или просто для создания случайных данных для разработки.
Библиотека имеет множество локализаций, так что вы можете генерировать данные в разных языках и форматах в зависимости от ваших потребностей.
"""
