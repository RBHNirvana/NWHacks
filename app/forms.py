from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, BooleanField, DateField, IntegerField, FloatField
from wtforms.validators import ValidationError, DataRequired, DataRequired, EqualTo, Length, Email


class OrgRegisterForm(FlaskForm):
  org_name = StringField("org_name", validators=[DataRequired()])
  password = PasswordField("password", validators=[DataRequired(), Length(min=8, max=80)])
  org_email = StringField("org_email", validators=[DataRequired(), Email()])
  submit = SubmitField('Register')

class PositionForm(FlaskForm):
  pos_name = StringField("pos_name", validators=[DataRequired()])
  pos_summary = StringField("pos_summary", validators=[DataRequired()])
  submit = SubmitField('Send')

class ApplicantForm(FlaskForm):
  name = StringField("name", validators=[DataRequired()])
  about = StringField("about", validators=[DataRequired()])
  city = StringField("city", validators=[DataRequired()])
  submit = SubmitField('Send')

class OrgLogin(FlaskForm):
  org_email = StringField("org_email", validators=[DataRequired(), Email()])
  password = PasswordField("password", validators=[DataRequired()])
  submit = SubmitField('Login')