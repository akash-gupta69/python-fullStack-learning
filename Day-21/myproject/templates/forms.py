from flask_wtf import FlaskForm
from wtforms import Stringfield, Submitfield, PasswordField 
from  wtforms.validators import Email, EqualTo, DataRequired
from wtforms import ValidationError
from .models import db, User

class LoginForm(FlaskForm):
    email = Stringfield("Email", validators=[DataRequired(),Email()])
    username = Stringfield("Username", validators=[DataRequired()])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    email = Stringfield("Email", validators=[DataRequired(),Email()])
    username = Stringfield("Username", validators=[DataRequired()])
    password =  Stringfield("Password", validators=[DataRequired(),EqualTo('pass_confirm')])
    submit = SubmitField("Login")

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError