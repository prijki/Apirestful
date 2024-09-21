from api import ma
from ..models import aluno_model
from marshmallow import fields

class AlunoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = aluno_model.Aluno
        load_instance = True
        fields = ("id","nome","data_nasc")

    nome = fields.String(required=True)
    data_nasc = fields.Date(required=True)

