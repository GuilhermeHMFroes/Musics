from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Musica(db.Model):
    __tablename__ = 'music'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80), nullable=False)
    artista = db.Column(db.String(80), nullable=False)
    video = db.Column(db.String(800), nullable=False)
    link = db.Column(db.String(800), nullable=False)
    genero = db.Column(db.String(80))

    def __repr__(self):
        return f'<Musica {self.titulo}>'
