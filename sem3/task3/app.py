"""📌 Доработаем задачy про студентов
📌 Создать базу данных для хранения информации о студентах и их оценках в
учебном заведении.
📌 База данных должна содержать две таблицы: "Студенты" и "Оценки".
📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
и email.
📌 В таблице "Оценки" должны быть следующие поля: id, id студента, название
предмета и оценка.
📌 Необходимо создать связь между таблицами "Студенты" и "Оценки".
📌 Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их оценок.
"""

from flask import Flask, render_template, jsonify
from models import db, Student, Grade
from random import randint
from faker import Faker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students_grades_db.db'

db.init_app(app)

fake = Faker('ru_RU')


@app.route('/')
def index():
    return 'Hi'


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_tables():
    count = 15

    # Добавляем студентов
    for _ in range(1, count + 1):

        new_std = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            group=randint(1001, 1022),
            email=fake.email()
        )
        db.session.add(new_std)
    db.session.commit()

    # Добавляем оценки

    for _ in range(1, count * 4):
        new_grade = Grade(
            id_student=randint(1, count+1),
            discipline=fake.word(ext_word_list=['физика', 'математика', 'химия', 'биология', 'история', 'физкультура']),
            grade=randint(2, 5)
        )

        db.session.add(new_grade)
    db.session.commit()


@app.route('/students/')
def get_std():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)

@app.route('/grade/student/<int:id_student>/')
def get_grade_by_std(id_student):
    grades = Grade.query.filter_by(id_student=id_student).all()
    std = Student.query.filter_by(id=id_student).first()

    if grades:
        return jsonify(
            [{'Студент ': std.last_name,'id': grade.id, 'Предмет': grade.discipline, 'Оценка': grade.grade} for grade in
             grades])
    else:
        return jsonify({'error': 'Posts not found'})


if __name__ == '__main__':
    app.run(debug=True)
