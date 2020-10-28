from flask import render_template
from main import bp
from main.auxiliar import atualiza_tabela


@bp.route('/')
def index():
    times = atualiza_tabela()
    return render_template('index.html', title='Classificação',
                           times=times)
