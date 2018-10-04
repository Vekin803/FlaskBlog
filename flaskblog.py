from flask import Flask, render_template, url_for, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bea1a01981dba12acea4fb565e5fc237'


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html")


@app.route("/about")
def hello():
    return render_template("about.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
    return render_template('register.html', title= 'Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title= 'Login', form=form)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
