# third-party imports
from flask import abort, Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Message, Mail

import os

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

# after the db variable initialization
login_manager = LoginManager()

#Flask-Mail initialization
mail = Mail()

def create_app(config_name):
    #init
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    #secret key
    app.secret_key = 'ldCz3GWmhos8QUJPGVt9'
    
    #db
    db.init_app(app)

    #mail
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = ''
    app.config["MAIL_PASSWORD"] = ''
    mail.init_app(app)
    
    #login manager
    login_manager.init_app(app)
    login_manager.login_message = "Você precisa estar logado para ver esta página."
    login_manager.login_view = "auth.login"

    Bootstrap(app)

    #blueprints

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .pessoas import pessoas as pessoas_blueprint
    app.register_blueprint(pessoas_blueprint, url_prefix='/pessoas')

    from .eventos import eventos as eventos_blueprint
    app.register_blueprint(eventos_blueprint, url_prefix='/eventos')
    
    #error handlers
    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    @app.route('/500')
    def error():
        abort(500)

    return app