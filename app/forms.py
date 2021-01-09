from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, BooleanField, DateField, IntegerField, FloatField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length, Email
from wtforms.widgets import ListWidget, CheckboxInput

#class FormName(FlaskForm):
  #field1 = ...
