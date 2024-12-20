from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='Enter Username:')
    email = StringField(label='Enter Email:')
    password1 = PasswordField(label= 'Enter Password:')
    password2 = PasswordField(label='Confirm Password:')
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label="Enter Username")
    password = PasswordField(label= 'Enter Password:')
    submit = SubmitField(label='Login')



