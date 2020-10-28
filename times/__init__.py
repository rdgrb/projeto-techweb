from flask import Blueprint

bp = Blueprint('times', __name__, template_folder='templates')

from times import routes
