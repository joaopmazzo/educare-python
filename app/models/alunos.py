from app import db
from sqlalchemy.orm import validates

class Alunos(db.Model):
  __tablename__ = 'alunos'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(80), unique=False, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  idade = db.Column(db.Integer, unique=False, nullable=True)
  
  matriculas = db.relationship(
    'matriculas',
    back_populates='alunos', 
    lazy='dynamic'  # Utiliza JOIN para relacionar com cursos
  )

  @validates('email')
  def validate_email(self, key, email):
    assert '@' in email, 'Formato de email invalido'
    return email