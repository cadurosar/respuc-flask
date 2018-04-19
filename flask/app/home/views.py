from flask import render_template, redirect, url_for

from flask_login import login_required, current_user

from . import home

@home.route('/test')
def test():
    return render_template('home/test.html')

@home.route('/')
def homepage():
    
    #Redirect pro login
    return redirect(url_for('auth.login'))

"""
@home.route('/dashboard')
@login_required
def dashboard():

    Render the dashboard template on the /dashboard route

    return render_template('home/dashboard.html', title="Dashboard")
"""