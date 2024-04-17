from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'3b1596d21b99a567c247e1c7f211e60df63986375d0c2e592c348c97fb7718dc'
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return 'Hi'



@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        print(first_name, last_name, email, password)
    return render_template('register.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)
