
"""📌 Создать базовый шаблон для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
📌 Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон."""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run()

