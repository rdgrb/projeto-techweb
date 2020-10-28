from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, ValidationError


class NovoJogoForm(FlaskForm):

    rodada = IntegerField('Rodada', validators=[DataRequired()])
    data = DateField('Data da Partida')
    vermelhos_mandante = IntegerField('Vermelhos', default=0)
    mandante = SelectField('Time Mandante', coerce=int)
    gols_mandante = IntegerField('Gols')
    amarelos_mandante = IntegerField('Amarelos', default=0)
    vermelhos_mandante = IntegerField('Vermelhos', default=0)
    visitante = SelectField('Time Visitante', coerce=int)
    gols_visitante = IntegerField('Gol')
    amarelos_visitante = IntegerField('Amarelos', default=0)
    vermelhos_visitante = IntegerField('Vermelhos', default=0)
    enviar = SubmitField('Enviar')

    def validate_visitante(self, visitante):
        if visitante.data == self.mandante.data:
            raise ValidationError('O Time mandante e o Visitante não podem'
                                  'ser o mesmo')

    def validate_rodada(self, rodada):
        if rodada.data > 10 or rodada.data < 0:
            raise ValidationError('Rodada Inválida')
