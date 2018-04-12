from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import Usuario

#FAZER (VERSAO DO EBEN ESSA; OLD)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        usuario = Usuario(email=form.email.data, usuario_id=form.usuario_id.data, nome=form.nome.data, senha=form.senha.data, e_coordenador=form.e_coordenador.data, e_professor=form.e_professor.data)

        db.session.add(usuario)
        db.session.commit()
        flash('Você foi registrado com sucesso! Agora você pode fazer login.')

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form, title='Registro')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario is not None and usuario.verify_senha(
                form.senha.data):
            login_user(usuario)
            if usuario.e_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))
        else:
            flash('Email ou senha inválidos.')

    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você fez logout com sucesso.')
    return redirect(url_for('auth.login'))
