from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Registeration(FlaskForm):
    username=StringField('User Name', validators=[DataRequired(),Length(min=2, max=20)])
    user_id=StringField('User Id', validators=[DataRequired(),Length(min=2, max=12)])
    email=StringField('Email', validators=[DataRequired(),Email(),Length(min=2, max=30)])
    password=PasswordField('Password', validators=[DataRequired(),Length(min=8)])
    confirm_password=PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')
    
class Login(FlaskForm):
    user_id=StringField('User Id', validators=[DataRequired(),Length(min=2, max=12)])
    password=PasswordField('Password', validators=[DataRequired(),Length(min=8)])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')