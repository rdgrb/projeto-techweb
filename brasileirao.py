from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import Config

# Faculdade Imapcta Tecnologia
# Tecnologia Web 02/2020 - ADS/BD
# Grupo XX:
# nome.sobrenome@aluno.faculdadeimpacta.com.br
# nome.sobrenome@aluno.faculdadeimpacta.com.br
# nome.sobrenome@aluno.faculdadeimpacta.com.br

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'auth.login'
bootstrap = Bootstrap(app)

from times import bp as times_bp
app.register_blueprint(times_bp, url_prefix='/times')

from jogos import bp as jogos_bp
app.register_blueprint(jogos_bp, url_prefix='/jogos')

from main import bp as main_bp
app.register_blueprint(main_bp)

from auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

with app.app_context():
    db.create_all()