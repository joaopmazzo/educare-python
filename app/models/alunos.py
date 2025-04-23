from app import db
from sqlalchemy.orm import validates


class Alunos(db.Model):
  __tablename__ = 'alunos'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(80))
  email = db.Column(db.String(120), unique=True)
  idade = db.Column(db.Integer)

  @validates('email')
  def validate_email(self, key, email):
    assert '@' in email, 'Formato de email invalido'
    return email
  
  def __repr__(self):
    return f'<Aluno {"id": self.id, "nome": self.nome}>'

  def to_dict(self):
    data = {
      "id": self.id,
      "nome": self.nome,
      "email": self.email,
      "idade": self.idade,
    }

    return data
