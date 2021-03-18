from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

class RegisterForm(FlaskForm):
    email = StringField("User Email", [DataRequired(), Email()])
    username = StringField("User Name",[DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("Sign In")

class LoginForm(FlaskForm):
    email = StringField("User Email", [DataRequired(), Email()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField('Log In')