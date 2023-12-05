from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, IntegerField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from api.models.models import Account

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
  is_keep_login = BooleanField('Keep Login')
  submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired(), Length(min=1, max=60)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

  submit = SubmitField("登録")
  
  def validate_email(self,email):
    mail = Account.query.filter_by(email= email.data).one_or_none()
    if mail is not None:
      raise ValidationError('このメールアドレスは既に登録されています。')