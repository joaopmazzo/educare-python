from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.schemas.AlunoSchema import AlunoSchema
from app.services.alunos_service import AlunosService

bp = Blueprint("alunos", __name__, url_prefix="/alunos")


@bp.route("/", methods=["GET"])
def get_alunos():
  try:
    alunos = AlunosService.get_all()
    return jsonify(
      [aluno.to_dict(include_matriculas=True) for aluno in alunos]
    ), 200
  except Exception as e:
    return jsonify({"error": str(e)}), 500


@bp.route("/", methods=["POST"])
def create_aluno():
  try:
    aluno_dto = AlunoSchema().load(request.get_json())
  except ValidationError as e:
    return jsonify({
      "error": e.messages,
      "dica": "Verifique os campos destacados"
    }), 400
  except Exception as e:
    return jsonify({"error": str(e)}), 500

  try:
    aluno = AlunosService.create(aluno_dto)
    return jsonify(aluno.to_dict()), 201
  except Exception as e:
    return jsonify({"error": str(e)}), 500
