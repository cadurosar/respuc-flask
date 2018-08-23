from flask import render_template, redirect, url_for, abort
from flask_login import login_required, current_user

from . import home
from ..models import Usuario

@home.route('/test')
def test():
    return render_template('home/test.html')

@home.route('/')
def homepage():
    
    #Redirect pro login
    return redirect(url_for('auth.login'))

@home.route('/dashboard')
def dashboard():

	return render_template('home/dashboard.html', title="Dashboard")

@home.route('/admin/dashboard')
def admin_dashboard():

	if not current_user.permissao == 1:
		abort(403)

	return render_template('home/admin_dashboard.html', title="Admin Dashboard")

"""
@home.route('/dashboard')
@login_required
def dashboard():

    Render the dashboard template on the /dashboard route

    return render_template('home/dashboard.html', title="Dashboard")
"""