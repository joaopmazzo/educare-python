from app import db
from app.models import Cursos
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


class CursosService:

  @staticmethod
  def get_all(page=0, per_page=10):
    try:
      return Cursos.query.paginate(page=page, per_page=per_page)
    except SQLAlchemyError as e:
      raise Exception("Falha ao retornar dados dos cursos") from e

  @staticmethod
  def create(curso_data):
    try:
      curso = Cursos(**curso_data)

      db.session.add(curso)
      db.session.commit()
      return curso
    except IntegrityError as e:
      db.session.rollback()

      if 'cursos.nome' in str(e.orig).lower():
        raise Exception("O nome de curso informado já está cadastrado")

      raise Exception("Erro de restrição do banco de dados") from e
    except SQLAlchemyError as e:
      db.session.rollback()
      raise Exception("Falha ao criar curso") from e
