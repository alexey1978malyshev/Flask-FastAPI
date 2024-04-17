from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'2061bc39d45c17f90be88990db767cab0969aa13b419059098b6ede83bc82b95'


# import secrets
# secrets.token_hex()

@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
# Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
# Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('students.html')

if __name__ == '__main__':
    app.run(debug=True)
