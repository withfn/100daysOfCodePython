from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, email_validator, Length
from flask_bootstrap import Bootstrap

class Login(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Invalid Email address")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Field must be at least 8 characters long.")])
    submit = SubmitField(label='Sign in')
    
user_email = "admin@email.com"
user_password = "12345678"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'eptaprdmv'
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET','POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        if form.email.data == user_email and form.password.data == user_password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)