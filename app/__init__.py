from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config.Config')

  db.init_app(app)
  migrate.init_app(app, db)

  from app.models import Alunos, Cursos, Matriculas
  
  with app.app_context():
    alunos = Alunos.query.first()
    print(alunos.to_dict(include_matriculas=True))

    cursos = Cursos.query.first()
    print(cursos.to_dict(include_matriculas=True))

    matriculas = Matriculas.query.first()
    print(matriculas.to_dict(include_aluno=True, include_curso=True))
  

  return app