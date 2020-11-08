from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from models import User

class LoginForm(FlaskForm):
    username = StringField('', validators=[DataRequired()])
    password = PasswordField('', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar-me', render_kw={"class": "form-check-input"})
    #submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Nome de Usuário"})
    email = StringField('', validators=[DataRequired(), Email()], render_kw={"placeholder": "E-mail"})
    password = PasswordField('', validators=[DataRequired()], render_kw={"placeholder": "Senha"})
    password2 = PasswordField(
        '', validators=[DataRequired(), EqualTo('password', "As senhas não conferem.")], render_kw={"placeholder": "Confirmar Senha"})
    #submit = SubmitField('Efetuar Registro', render_kw={"class": "btn-info"})

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Esse usuário já foi usado.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Esse e-mail já foi usado por outra conta.')
