from app import db

class Alunos(db.Model):
  __tablename__ = 'alunos'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(80), unique=False, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  idade = db.Column(db.Integer, unique=False, nullable=True)