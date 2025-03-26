from marshmallow import Schema, fields, validate


class AlunoSchema(Schema):
  nome = fields.Str(
    required=True,
    validate=validate.Length(min=2, max=80, error="O nome deve ter entre 2 e 80 caracteres"),
    error_messages={
      "required": "Por favor, informe o nome do aluno",
      "invalid": "O nome deve ser um texto valido"
    }
  )
  email = fields.Email(
    required=True,
    error_messages={
      "required": "Por favor, informe o e-mail do aluno",
      "invalid": "E-mail invalido (exemplo: aluno@escola.com)"
    }
  )
  idade = fields.Int(
    required=True,
    error_messages={
      "required": "Por favor, informe a idade do aluno",
      "invalid": "A idade deve ser um numero (exemplo: 25)"
    }
  )
