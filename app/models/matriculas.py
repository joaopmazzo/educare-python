from app import db


class Matriculas(db.Model):
  __tablename__ = 'matriculas'

  aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), primary_key=True)
  curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), primary_key=True)
  data_matricula = db.Column(db.DateTime, default=db.func.current_timestamp())
  nota = db.Column(db.String(2))

  aluno = db.relationship("Alunos", back_populates="matriculas")
  curso = db.relationship("Cursos", back_populates="matriculas")

  def to_dict(self, include_aluno=False, include_curso=False):
    data = {
      "data_matricula": self.data_matricula.isoformat() if self.data_matricula else None,
      "nota": self.nota,
    }

    if include_aluno:
      data["aluno"] = self.aluno.to_dict() if self.aluno else None

    if include_curso:
      data["curso"] = self.curso.to_dict() if self.curso else None

    return data
