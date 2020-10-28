from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from jogos import bp
from jogos.forms import NovoJogoForm
from models import Jogo, Time
from brasileirao import db
from sqlalchemy.exc import IntegrityError


@bp.route('/')
@login_required
def index():
    jogos = Jogo.jogos_rodada()
    return render_template('listarjogos.html', title='Jogos', jogos=jogos)


@bp.route('/new', methods=['GET', 'POST'])
@login_required
def create():
    form = NovoJogoForm()
    times = list(Time.query.with_entities(Time.id, Time.nome))
    form.mandante.choices = times
    form.visitante.choices = times
    if form.validate_on_submit():
        jogo = Jogo(rodada=form.rodada.data, data=form.data.data,
                    time_mandante_id=form.mandante.data,
                    gols_mandante=form.gols_mandante.data,
                    amarelos_mandante=form.amarelos_mandante.data,
                    vermelhos_mandante=form.vermelhos_mandante.data,
                    time_visitante_id=form.visitante.data,
                    gols_visitante=form.gols_visitante.data,
                    amarelos_visitante=form.amarelos_visitante.data,
                    vermelhos_visitante=form.vermelhos_visitante.data)
        try:
            db.session.add(jogo)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            e = {'Duplicidade': ["Esta partida já ocorrreu"]}
            return render_template('novojogo.html', title='Novo Jogo',
                                   form=form, jogo=None, errors=e)
        else:
            return redirect(url_for('jogos.index'))
    return render_template('novojogo.html', title='Novo Jogo', form=form,
                           jogo=None, errors=form.errors)


@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def update(id):
    jogo = Jogo.query.get_or_404(id)
    form = NovoJogoForm()
    times = list(Time.query.with_entities(Time.id, Time.nome))
    form.mandante.choices = times
    form.visitante.choices = times
    if form.validate_on_submit():
        jogo.rodada = form.rodada.data
        jogo.data = form.data.data
        jogo.time_mandante_id = form.mandante.data
        jogo.gols_mandante = form.gols_mandante.data
        jogo.amarelos_mandante = form.amarelos_mandante.data
        jogo.vermelhos_mandante = form.vermelhos_mandante.data
        jogo.time_visitante_id = form.visitante.data
        jogo.gols_visitante = form.gols_visitante.data
        jogo.amarelos_visitante = form.amarelos_visitante.data
        jogo.vermelhos_visitante = form.vermelhos_visitante.data
        db.session.add(jogo)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('jogos.index'))
    elif request.method == 'GET':
        form.rodada.data = jogo.rodada
        form.data.data = jogo.data
        form.mandante.data = jogo.time_mandante_id
        form.gols_mandante.data = jogo.gols_mandante
        form.amarelos_mandante.data = jogo.amarelos_mandante
        form.vermelhos_mandante.data = jogo.vermelhos_mandante
        form.visitante.data = jogo.time_visitante_id
        form.gols_visitante.data = jogo.gols_visitante
        form.amarelos_visitante.data = jogo.amarelos_visitante
        form.vermelhos_visitante.data = jogo.vermelhos_visitante
    return render_template('novojogo.html', form=form, title="Editar Jogo",
                           jogo=jogo, errors=form.errors)


@bp.route('/<int:id>/delete')
@login_required
def delete(id):
    jogo = Jogo.query.get_or_404(id)
    db.session.delete(jogo)
    db.session.commit()
    return redirect(url_for('jogos.index'))
