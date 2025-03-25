from app import db

class Cursos(db.Model):
  __tablename__ = 'cursos'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(80), unique=False, nullable=False)
  carga_horaria = db.Column(db.Integer, unique=False, nullable=False)

  matriculas = db.relationship(
    'matriculas',
    backref='cursos',
    lazy='dynamic'
  )