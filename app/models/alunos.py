from app import db
from sqlalchemy.orm import validates


class Alunos(db.Model):
  __tablename__ = 'alunos'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(80))
  email = db.Column(db.String(120), unique=True)
  idade = db.Column(db.Integer)

  matriculas = db.relationship(
    "Matriculas",
    back_populates="aluno",
    lazy="dynamic"
  )

  @validates('email')
  def validate_email(self, key, email):
    assert '@' in email, 'Formato de email invalido'
    return email

  def to_dict(self, include_matriculas=False):
    data = {
      "id": self.id,
      "nome": self.nome,
      "email": self.email,
      "idade": self.idade,
    }

    if include_matriculas:
      data["matriculas"] = [m.to_dict(include_curso=True) for m in self.matriculas]

    return data
