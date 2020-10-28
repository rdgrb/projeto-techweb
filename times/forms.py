from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from models import Time


class NovoTimeForm(FlaskForm):

    nome_time = StringField('Nome do Time',
                            validators=[DataRequired(), Length(min=3, max=50)])
    escudo = StringField('Link Escudo')
    enviar = SubmitField('enviar')

    def __init__(self, nome_original=None, *args, **kwargs):
        super(NovoTimeForm, self).__init__(*args, **kwargs)
        self.nome_original = nome_original

    def validate_nome_time(self, nome_time):
        if self.nome_original is None or \
           self.nome_original != self.nome_time.data:
            time = Time.query.filter_by(nome=nome_time.data).first()
            if time is not None:
                raise ValidationError('Esse time já existe')
