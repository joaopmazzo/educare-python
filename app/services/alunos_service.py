from app import db
from app.models import Alunos
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


class AlunosService:

  @staticmethod
  def get_all(page=0, per_page=10):
    try:
      return Alunos.query.paginate(page=page, per_page=per_page)
    except SQLAlchemyError as e:
      raise Exception("Falha ao retornar dados dos alunos") from e

  @staticmethod
  def create(aluno_data):
    try:
      aluno = Alunos(**aluno_data)

      db.session.add(aluno)
      db.session.commit()
      return aluno
    except IntegrityError as e:
      db.session.rollback()

      if 'alunos.email' in str(e.orig).lower():
        raise Exception("O e-mail informado já está cadastrado")

      raise Exception("Erro de restrição do banco de dados") from e
    except SQLAlchemyError as e:
      db.session.rollback()
      raise Exception("Falha ao criar aluno") from e
