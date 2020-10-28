from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from times import bp
from times.forms import NovoTimeForm
from models import Time
from brasileirao import db


@bp.route('/')
@login_required
def index():
    times = Time.query.order_by(Time.nome).all()
    return render_template('listar.html', title='Times', times=times)


@bp.route('/new', methods=['GET', 'POST'])
@login_required
def create():
    form = NovoTimeForm()
    if form.validate_on_submit():
        time = Time(nome=form.nome_time.data, escudo=form.escudo.data)
        db.session.add(time)
        db.session.commit()
        return redirect(url_for('times.index'))
    return render_template('novotime.html', title='Novo Time', form=form)

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def update(id):

    time = Time.query.get_or_404(id)
    form = NovoTimeForm(nome_original=time.nome)
    if form.validate_on_submit():
        time.nome = form.nome_time.data
        time.escudo = form.escudo.data
        db.session.add(time)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('times.index'))
    elif request.method == 'GET':
        time = Time.query.get(id)
        form.nome_time.data = time.nome
        form.escudo.data = time.escudo
    return render_template('novotime.html', form=form, title='Editar Time')


@bp.route('/<int:id>/delete')
@login_required
def delete(id):
    time = Time.query.get_or_404(id)
    db.session.delete(time)
    db.session.commit()
    return redirect(url_for('times.index'))
