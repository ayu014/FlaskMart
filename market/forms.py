from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(f"{username_to_check.data} aleady exists. Please try a different username.")
    
    def validate_email(self,email_to_check):
        email_address = User.query.filter_by(email=email_to_check.data).first()
        if email_address:
            raise ValidationError(f"{email_to_check.data} is associated with another account. Please try different email.")
    

    username = StringField(label='Enter Username:',validators=[Length(min=3,max=12), DataRequired()])
    email = StringField(label='Enter Email:',validators=[Length(min=3,max=50), Email(), DataRequired()])
    password1 = PasswordField(label= 'Enter Password:',validators=[Length(min=8,max=60), DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label="Username:",validators=[Length(min=3),DataRequired()])
    password = PasswordField(label= 'Password:', validators=[Length(min=8),DataRequired()])
    submit = SubmitField(label='Login')



