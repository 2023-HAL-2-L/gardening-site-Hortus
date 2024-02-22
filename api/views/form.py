from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    TextAreaField,
    SelectField,
    IntegerField,
    FileField,
)
from flask_wtf.file import FileRequired
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, NumberRange
from api.models.models import Account


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="この項目は入力が必須です。"),
            Email(message="有効なメールアドレスを入れてください。"),
            Length(min=1, max=63, message = "1から63文字の有効な値を入れてください。"),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(message="この項目は入力が必須です"), Length(min=6, max=63, message="6から63文字の有効な値を入れてください。")],
    )
    is_keep_login = BooleanField("ログインを記録する")
    submit = SubmitField("ログイン")
    


class RegistrationForm(FlaskForm):
    name = StringField(
        "名前", validators=[DataRequired(message="この項目は入力が必須です"), Length(min=1, max=60, message="1から60文字の有効な値を入れてください。")]
    )
    email = StringField(
        "Email", validators=[DataRequired(message="この項目は入力が必須です"), Email(message="有効なメールアドレスを入れてください。")]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(message="この項目は入力が必須です"), Length(min=6, max=20, message="6から20文字の有効な値を入れてください。")],
    )
    confirm_password = PasswordField(
        "Password再確認",
        validators=[DataRequired(message="この項目は入力が必須です"), EqualTo("password")],
    )
    # address = StringField('住所', validators=[DataRequired(message="この項目は入力が必須です"), Length(min=1, max=256)])
    submit = SubmitField("登録")

    def validate_email(self, email):
        mail = Account.query.filter_by(email=email.data).one_or_none()
        if mail is not None:
            raise ValidationError("このメールアドレスは既に登録されています。")


class ProductSearchForm(FlaskForm):
    name = StringField("商品名", validators=[Length(min=1, max=60, message="1から60文字の有効な値を入れてください。")])
    submit = SubmitField("検索")

class ExhibitProductForm(FlaskForm):
    name = StringField("商品名", validators=[DataRequired(message="この項目は入力が必須です"), Length(min=2, max=60, message="2から60文字の有効な値を入れてください。")])
    image = FileField("商品画像", validators=[DataRequired(message="この項目は入力が必須です"),FileRequired(message="この項目は入力が必須です")])
    price = IntegerField("商品価格", validators=[DataRequired(message="この項目は入力が必須です"), NumberRange(min=0, message="有効な値を入れてください。")], render_kw={"placeholder": "0", "min": "0"})
    description = TextAreaField("商品の説明", validators=[DataRequired(message="この項目は入力が必須です"), Length(max=1023, message="1023文字までの有効な値を入れてください。")])
    category = SelectField("商品カテゴリ", choices=[("1", "生花"), ("2", "種"), ("3", "その他")])
    # condition = SelectField("商品状態", choices=[("1", "つぼみ"), ("2", "咲いている"), ("3", "種"), ("4", "その他")])
    shipping_days = SelectField("発送までの日数", choices=[("1", "1日〜2日"), ("2", "2日〜3日"), ("3", "4日〜7日"), ("4", "1週間以上")])
    is_barter = BooleanField("物々交換を許可する")
    submit = SubmitField("出品する")