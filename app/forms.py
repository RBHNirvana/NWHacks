from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, BooleanField, DateField, IntegerField, FloatField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length, Email, InputRequired
from wtforms.widgets import ListWidget, CheckboxInput

#class FormName(FlaskForm):
  #field1 = ...
class OrgRegisterForm(FlaskForm):
  org_name = StringField("org_name", validators=[InputRequired()])
  password = PasswordField("password", validators=[InputRequired(), Length(min=8, max=80)])
  org_email = StringField("org_email", validators=[InputRequired(), Email()])
  submit = SubmitField('Register')

class PositionForm(FlaskForm):
  pos_name = StringField("pos_name", validators=[InputRequired()])
  pos_summary = StringField("pos_summary", validators=[InputRequired()])
  submit = SubmitField('Send')

class ApplicantForm(FlaskForm):
  name = StringField("name", validators=[InputRequired()])
  about = StringField("about", validators=[InputRequired()])
  city = StringField("city", validators=[InputRequired()])
  submit = SubmitField('Send')

class OrgLogin(FlaskForm):
  org_email = StringField("org_email", validators=[DataRequired(), Email()])
  password = PasswordField("password", validators=[InputRequired()])
  submit = SubmitField('Login')