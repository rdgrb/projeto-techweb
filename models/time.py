from brasileirao import db


class Time(db.Model):
    __tablename__ = 'times'
    id = db.Column(db.Integer, primary_key=True)
    escudo = db.Column(db.String)
    nome = db.Column(db.String(20), index=True, unique=True)

    @property
    def jogos(self):
        return sorted(self.jogos_mandante + self.jogos_visitante,
                      key=lambda x: x.data)

    def __repr__(self):
        return f'<Time: {self.nome}>'
