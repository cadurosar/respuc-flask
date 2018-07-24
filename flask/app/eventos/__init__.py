from flask import Blueprint

eventos = Blueprint('eventos', __name__)

from . import views
