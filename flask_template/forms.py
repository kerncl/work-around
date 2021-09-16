from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField,SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError


class ContactForm(Form):
    name = TextField("Name Of Students", [validators.Required("PLease enter your name")])
    Gender = RadioField('Gender', choices=[('M','Male'), ('F','Femaile')])
    Address = TextAreaField('Address')
    email = TextField("Email",
                      [validators.Required("Please enter your email address."),
                      validators.Email("Please enter your email address.")])
    Age = IntegerField('age')
    language = SelectField('Language', choices=[('cpp','c++'), ('py', 'Python')])
    submit = SubmitField("Send")