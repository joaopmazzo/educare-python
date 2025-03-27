from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.schemas.AlunoSchema import AlunoSchema
from app.services import AlunosService

bp = Blueprint("alunos", __name__, url_prefix="/alunos")


@bp.route("/", methods=["GET"])
def get_alunos():
  try:
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    alunos_paginados = AlunosService.get_all(page=page, per_page=per_page)
    return jsonify({
      "content": [aluno.to_dict(include_matriculas=True) for aluno in alunos_paginados],
      "total": alunos_paginados.total,
      "pages": alunos_paginados.pages,
      "current_page": page,
      "per_page": per_page 
    }), 200
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
