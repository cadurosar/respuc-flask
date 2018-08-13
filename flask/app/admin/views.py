from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user

from . import admin
from .. import db
from ..models import Usuario

@admin.route('/admin/dashboard')
def aprovar_usuarios():

	if not current_user.role == "admin":
		abort(403)

	usuarios = Usuario.query.filter_by(confirmado=False).all()


	return render_template('admin/aprovar_usuarios.html', title="Admin Dashboard", usuarios=usuarios)