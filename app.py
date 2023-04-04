from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from models import db, Musica
from controllers.musica import musica_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://teste:teste@localhost/music'

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(musica_bp)

@app.route('/')
def index():
    musicas = Musica.query.all()
    if not musicas:
        return render_template('index.html', mensagem='Nenhuma música cadastrada')
    else:
        return render_template('index.html', musicas=musicas)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/deletar')
def deletar():
    musicas = Musica.query.all()
    if not musicas:
        return render_template('deletar.html', mensagem='Nenhuma música cadastrada')
    else:
        return render_template('deletar.html', musicas=musicas)
    #return render_template('deletar.html')
