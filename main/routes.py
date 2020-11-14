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

    def checar_rebaixamento(index, qnt_times):
        lista_rebaixada = [qnt_times, qnt_times -
                           1, qnt_times - 2, qnt_times - 3]
        for indice in lista_rebaixada:
            if index == (indice - 1):
                return True

        return False

    show_modal = True
    times = atualiza_tabela()
    return render_template('index.html', title='Classificação',
                           times=times, qnt_times=len(times),
                           situacao_time=situacao_time,
                           checar_rebaixamento=checar_rebaixamento,
                           show_modal=show_modal)
