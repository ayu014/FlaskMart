from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='Enter Username:',validators=[Length(min=3,max=12), DataRequired()])
    email = StringField(label='Enter Email:',validators=[Length(min=3,max=20), Email(), DataRequired()])
    password1 = PasswordField(label= 'Enter Password:',validators=[Length(min=8,max=60), DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label="Enter Username:")
    password = PasswordField(label= 'Enter Password:')
    submit = SubmitField(label='Login')



