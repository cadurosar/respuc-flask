from flask import Blueprint

pessoas = Blueprint('pessoas', __name__)

from . import views
