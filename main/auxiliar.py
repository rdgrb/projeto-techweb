from models import Jogo, Time


def inicializa_time(time):
    time.empates = 0
    time.vitorias = 0
    time.pontos = 0
    time.cartoes_amarelos = 0
    time.cartoes_vermelhos = 0
    time.gols_contra = 0
    time.gols_pro = 0
    time.saldo_gols = 0
    time.derrotas = 0


def atualiza_tabela():
    times = Time.query.all()
    for time in times:
        inicializa_time(time)
    for jogo in Jogo.query.all():
        m = jogo.mandante
        v = jogo.visitante
        m.gols_pro += jogo.gols_mandante
        v.gols_contra += jogo.gols_mandante
        v.gols_pro += jogo.gols_visitante
        m.gols_contra += jogo.gols_visitante
        v.saldo_gols = v.saldo_gols + jogo.gols_visitante - jogo.gols_mandante
        m.saldo_gols = m.saldo_gols - jogo.gols_visitante + jogo.gols_mandante
        m.cartoes_amarelos += jogo.amarelos_mandante
        v.cartoes_amarelos += jogo.amarelos_visitante
        m.cartoes_vermelhos += jogo.vermelhos_mandante
        v.cartoes_vermelhos += jogo.vermelhos_visitante
        if jogo.gols_visitante < jogo.gols_mandante:
            m.pontos += 3
            m.vitorias += 1
            v.derrotas += 1
        elif jogo.gols_visitante > jogo.gols_mandante:
            v.pontos += 3
            v.vitorias += 1
            m.derrotas += 1
        else:
            m.pontos += 1
            m.empates += 1
            v.pontos += 1
            v.empates += 1
    return sorted(times,
                  key=lambda x: (-x.pontos, -x.vitorias, -x.saldo_gols,
                                 -x.gols_pro, x.cartoes_vermelhos,
                                 x.cartoes_amarelos))
