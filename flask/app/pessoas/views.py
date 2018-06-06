from flask import flash, redirect, render_template, url_for
from flask_login import login_required

from . import pessoas
from .. import db
from ..models import Usuario

@pessoas.route('/', methods=['GET', 'POST'])