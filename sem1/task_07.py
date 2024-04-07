


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    _news_block = [
        {'title' :'Сегодня в мире',
         'describe': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi, odit?',
         'date': '06/04/2024'
         },
        {'title':'Новости искуства',
         'describe': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi, odit?',
         'date': '07/04/2024'
         },
        {'title' :'Новости спорта',
         'describe': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi, odit?',
         'date': '05/04/2024'
         },
    ]
    context = {'news_block': _news_block}

    return render_template('news_block.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
