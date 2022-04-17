from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from flask_market.Model import User

class RegisterForm(FlaskForm):
    def validate_Username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('user alteady exist,so try with any other name')
    def validate_email_address(self,email_address_to_check):
        email=User.query.filter_by(email_address=email_address_to_check.data).first()
        if email:
            raise ValidationError('email already exit ,try with some other email')
    Username=StringField(label="User Name",validators=[Length(min=3,max=20),DataRequired()])
    email_address=StringField(label="Email address",validators=[Email(),DataRequired()])
    passward1=PasswordField(label="passward",validators=[Length(min=5),DataRequired()])
    passward2=PasswordField(label="confirm passward",validators=[EqualTo('passward1'),DataRequired()])
    submit=SubmitField(label="Create account")

class LoginForm(FlaskForm):
    username=StringField(label="User Name",validators=[DataRequired()])
    passward=PasswordField(label="passward",validators=[DataRequired()])
    submit=SubmitField(label="sign in")

class PurchaseItemForm(FlaskForm):
    Submit=SubmitField(label="Purchase item")

class SellItemForm(FlaskForm):
    Submit=SubmitField(label="Sell item")




