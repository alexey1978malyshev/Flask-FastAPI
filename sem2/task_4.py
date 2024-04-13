"""📌 Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
📌 При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом."""

from flask import Flask, request, render_template,redirect


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        cnt_wrd = len(request.form.get('input').split())
        context = {'count': cnt_wrd}
        return render_template('len_txt.html', **context)
    return render_template('form_txt_input.html')


if __name__ == '__main__':
    app.run(debug=True)
