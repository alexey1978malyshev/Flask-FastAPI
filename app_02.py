from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Привет, незнакомец'

@app.route('/Полина/')
def polina():
    return 'Привет, Полина!'


@app.route('/Ульяна/')
def ulyana():
    return 'Привет, Ульяна!!'

@app.route('/Степан/')
def stepan():
    return 'Привет, Степан!!'

if __name__=='__main__':
    app.run()