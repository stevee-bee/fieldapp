from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField, IntegerField, DateField, DecimalField, HiddenField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length

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
    number = IntegerField('Field number', validators=[DataRequired()])
    name = StringField('Field name', validators=[DataRequired()])
    land_loc = StringField('Land location')
    comment = TextAreaField('Comments', validators=[Length(max=255)])
    submit = SubmitField('Save')

    def validate_number(self, number):
        field = Field.query.filter_by(number=number.data).first()
        if field is not None:
            raise ValidationError('This field number is already used. Please enter a different number.')


class FieldFormEdit(FlaskForm):
    number = HiddenField('Field number', validators=[DataRequired()])
    name = StringField('Field name', validators=[DataRequired()])
    land_loc = StringField('Land location')
    comment = TextAreaField('Comments', validators=[Length(max=255)])
    submit = SubmitField('Save')


class SeedFormAdd(FlaskForm):
    date_seeded = DateField('Date seeded', validators=[DataRequired()])
    name = StringField('Seed', validators=[DataRequired()])
    comment = TextAreaField('Comments', validators=[Length(max=255)])
    submit = SubmitField('Save')


class SeedFormEdit(FlaskForm):
    date_seeded = DateField('Date seeded', validators=[DataRequired()])
    name = StringField('Seed', validators=[DataRequired()])
    date_harvested = DateField('Date harvested')
    bu_yield = DecimalField('Yield', places=1)
    comment = TextAreaField('Comments', validators=[Length(max=255)])
    submit = SubmitField('Save')


class ChemicalForm(FlaskForm):
    type = SelectField('Type', choices=[(0,'Fungicide'), (1,'Herbicide'), (2,'Insecticide')], validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    date_applied = DateField('Date applied', validators=[DataRequired()])
    rate = DecimalField('Rate')
    wind_dir = StringField('Wind direction')
    comment = TextAreaField('Comments', validators=[Length(max=255)])
    submit = SubmitField('Save')
