from app import db


class Cursos(db.Model):
  __tablename__ = 'cursos'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(80), unique=False, nullable=False)
  carga_horaria = db.Column(db.Integer, unique=False, nullable=False)

  matriculas = db.relationship(
    'Matriculas',
    back_populates='curso',
    lazy='dynamic'
  )

  def __repr__(self):
    return f'<Curso {"id": self.id, "nome": self.nome}>'

  def to_dict(self, include_matriculas=False):
    data = {
      "id": self.id,
      "nome": self.nome,
      "carga_horaria": self.carga_horaria,
    }

    if include_matriculas:
      data["matriculas"] = data["matriculas"] = [m.to_dict(include_aluno=True) for m in self.matriculas]

    return data
