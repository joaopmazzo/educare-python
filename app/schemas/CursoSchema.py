from marshmallow import Schema, fields, validate


class CursoSchema(Schema):
  nome = fields.Str(
    required=True,
    validate=validate.Length(min=2, max=80, error="O nome deve ter entre 2 e 80 caracteres"),
    error_messages={
      "required": "Por favor, informe o nome do curso",
      "invalid": "O nome deve ser um texto valido"
    }
  )
  carga_horaria = fields.Int(
    required=True,
    error_messages={
      "required": "Por favor, informe a carga horaria do curso",
      "invalid": "A carga horaria deve ser um numero (exemplo: 40)"
    }
  )
