from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from models import User, Field


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('The username chosen is already used. Please enter a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('The email chosen is already used. Please enter a different email address.')


class FieldForm(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    land_loc = StringField('Land location')
    comment = TextAreaField('Comments')
    submit = SubmitField('Create field')

    def validate_number(self, number):
        field = Field.query.filter_by(number=number.data).first()
        if field is not None:
            raise ValidationError('This field number is already used. Please enter a different number.')


# class SeedForm(FlaskForm):
#     seedname = StringField('Seed', validators=[DataRequired()])
#     seeddate =
#     harvestdate =
#     harvestyield =


# class ChemicalForm(FlaskForm):
#     chemtype = ... validators=[AnyOf( -provide list from db- )] ...
#     chemname =
#     rate =
#     chemdate =

