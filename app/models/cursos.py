from app import db


class Cursos(db.Model):
  __tablename__ = 'cursos'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(80), unique=True, nullable=False)
  carga_horaria = db.Column(db.Integer, unique=False, nullable=False)

  def __repr__(self):
    return f'<Curso {"id": self.id, "nome": self.nome}>'

  def to_dict(self):
    data = {
      "id": self.id,
      "nome": self.nome,
      "carga_horaria": self.carga_horaria,
    }

    return data
