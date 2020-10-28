from brasileirao import db


class Jogo(db.Model):
    __tablename__ = 'jogos'
    id = db.Column(db.Integer, primary_key=True)
    rodada = db.Column(db.Integer)
    data = db.Column(db.Date)
    time_visitante_id = db.Column(db.Integer, db.ForeignKey('times.id'))
    time_mandante_id = db.Column(db.Integer, db.ForeignKey('times.id'))
    gols_mandante = db.Column(db.Integer, default=0)
    gols_visitante = db.Column(db.Integer, default=0)
    amarelos_mandante = db.Column(db.Integer, default=0)
    amarelos_visitante = db.Column(db.Integer, default=0)
    vermelhos_mandante = db.Column(db.Integer, default=0)
    vermelhos_visitante = db.Column(db.Integer, default=0)
    uix_1 = db.UniqueConstraint(time_visitante_id, time_mandante_id)
    mandante = db.relationship('Time', foreign_keys=[time_mandante_id],
                               backref=db.backref('jogos_mandante'))
    visitante = db.relationship('Time', foreign_keys=[time_visitante_id],
                                backref=db.backref('jogos_visitante'))

    @classmethod
    def jogos_rodada(cls):
        rodadas = 10
        jogos = {}
        for i in range(1, rodadas + 1):
            partidas = cls.query.filter_by(rodada=i) \
                          .order_by(Jogo.data).all()
            jogos[i] = partidas
        return jogos

    def __repr__(self):
        return f'<Jogo: {self.mandante} {self.gols_mandante} x' \
            f'{self.gols_visitante} {self.visitante}>'
