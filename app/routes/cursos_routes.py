from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.schemas.CursoSchema import CursoSchema
from app.services import CursosService

bp = Blueprint("cursos", __name__, url_prefix="/cursos")


@bp.route("/", methods=["GET"])
def get_alunos():
  try:
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    cursos_paginados = CursosService.get_all(page=page, per_page=per_page)
    return jsonify({
      "content": [curso.to_dict() for curso in cursos_paginados],
      "total": cursos_paginados.total,
      "pages": cursos_paginados.pages,
      "current_page": page,
      "per_page": per_page 
    }), 200
  except Exception as e:
    return jsonify({"error": str(e)}), 500


@bp.route("/", methods=["POST"])
def create_aluno():
  try:
    curso_dto = CursoSchema().load(request.get_json())
  except ValidationError as e:
    return jsonify({
      "error": e.messages,
      "dica": "Verifique os campos destacados"
    }), 400
  except Exception as e:
    return jsonify({"error": str(e)}), 500

  try:
    curso = CursosService.create(curso_dto)
    return jsonify(curso.to_dict()), 201
  except Exception as e:
    return jsonify({"error": str(e)}), 500
