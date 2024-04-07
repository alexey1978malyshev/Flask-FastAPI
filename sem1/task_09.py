"""📌 Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров.
📌 Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон. """


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Главная'
    context = {'title': title}
    return render_template('main_shop.html', **context)

@app.route('/wear/')
def wear():
    title = 'Одежда'
    context = {'title': title}
    return render_template('wear.html', **context)

@app.route('/shoes/')
def shoes():
    title = 'Обувь'
    context = {'title': title}
    return render_template('shoes.html', **context)

@app.route('/coat/')
def coat():
    title = 'Плащ'
    context = {'title': title}
    return render_template('coat.html', **context)

if __name__ == '__main__':
    app.run()