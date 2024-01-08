from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, IntegerField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from api.models.models import Account

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(message="この項目は入力が必須です"), Email(), Length(min=1, max=63)])
  password = PasswordField('Password', validators=[DataRequired(message="この項目は入力が必須です"), Length(min=6, max=63)])
  is_keep_login = BooleanField('ログインを記録する')
  submit = SubmitField("ログイン")

class RegistrationForm(FlaskForm):
  name = StringField('名前', validators=[DataRequired(message="この項目は入力が必須です"), Length(min=1, max=60)])
  email = StringField('Email', validators=[DataRequired(message="この項目は入力が必須です"), Email()])
  password = PasswordField('Password', validators=[DataRequired(message="この項目は入力が必須です"), Length(min=6, max=20)])
  confirm_password = PasswordField('Password再確認', validators=[DataRequired(message="この項目は入力が必須です"), EqualTo('password')])
  # address = StringField('住所', validators=[DataRequired(message="この項目は入力が必須です"), Length(min=1, max=256)])
  submit = SubmitField("登録")
  
  def validate_email(self,email):
    mail = Account.query.filter_by(email= email.data).one_or_none()
    if mail is not None:
      raise ValidationError('このメールアドレスは既に登録されています')

class productSearchForm(FlaskForm):
  product_name = StringField('商品名', Length(min=1, max=60))
  submit = SubmitField("検索")