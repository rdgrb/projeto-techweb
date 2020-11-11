from flask import render_template
from main import bp
from main.auxiliar import atualiza_tabela


@bp.route('/')
def index():
    def situacao_time(index, lista_indices):
        for indice in lista_indices:
            if index == indice:
                return True 
        
        return False 

    show_modal = True 
    times = atualiza_tabela()
    return render_template('index.html', title='Classificação',
                           times=times, qnt_times=len(times),
                           situacao_time=situacao_time,
                           show_modal=show_modal)
