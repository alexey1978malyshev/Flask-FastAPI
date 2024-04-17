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
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=True, nullable=False)
    last_name = db.Column(db.String(60), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    group = db.Column(db.String(10), nullable=False)
    id_faculty = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self):
        return f'Student - name:{self.last_name} {self.first_name} '


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f'Faculty:{self.id} {self.faculty_name} '
