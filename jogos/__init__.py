from flask import Blueprint

bp = Blueprint('jogos', __name__, template_folder='./templates')

from jogos import routes
