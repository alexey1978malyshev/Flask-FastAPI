
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    group = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    grades = db.relationship('Grade', backref='student', lazy=True)

    def __repr__(self):
        return f'Student - name:{self.last_name} {self.first_name} '


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_student = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    discipline = db.Column(db.String(20), unique=False, nullable=False)
    grade = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f'id_student: {self.id_student} - {self.discipline} / {self.grade}'
