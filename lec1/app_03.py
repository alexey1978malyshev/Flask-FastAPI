from flask import Flask

app = Flask(__name__)

@app.route('/')
def imdex():
    return "Hi!"

@app.route('/Степан/')
@app.route('/Степа/')
@app.route('/Стёпа/')
def stepan():
    return 'Привет, Стёпа!'


if __name__=='__main__':
    app.run()