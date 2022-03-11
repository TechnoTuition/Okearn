from wtforms import Form,StringField,IntegerField,PasswordField , validators
from wtforms.validators import EqualTo,DataRequired,Email,Length
from flask_wtf import FlaskForm
class RegisterForm(FlaskForm):
  firstname = StringField('First Name',validators=[DataRequired(),Length(min=3)])
  lastname = StringField('Last Name',validators=[DataRequired(),Length(min=3)])
  email = StringField('Email',validators=[DataRequired(),Email(message=('That\'s not a valid email address.')),Length(min=6)])
  password = PasswordField('Password',validators=[DataRequired(),Length(min=6)])

class LoginForm(FlaskForm):
  email = StringField('Email',validators=[DataRequired(),Email(message=('That\'s not a valid email address.')),Length(min=6)])
  password = PasswordField('Password',validators=[DataRequired(),Length(min=6)])
  
class EmailVerificationForm(FlaskForm):
  code = StringField('Email Verification',validators=[DataRequired()])