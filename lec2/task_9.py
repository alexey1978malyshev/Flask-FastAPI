import logging
from flask import Flask, render_template, request, abort
from get_block import get_blog

app = Flask(__name__)
logger = logging.getLogger(__name__)

login = Alex
password = qwe


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


@app.route('/blog/<int:id>')
def get_blog_by_id(id):
    # делаем запрос в БД для поиска статьи по id
    result = get_blog(id)
    if result is None:
        abort(404)


# возвращаем найденную в БД статью
@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)

    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('p404.html', **context), 404

if __name__ == '__main__':
    app.run(debug=True)
