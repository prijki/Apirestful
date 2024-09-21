from api import ma
from ..models import professor_model
from marshmallow import fields

class ProfessorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = professor_model.Professor
        load_instance = True
        fields = ("id","nome","data_nasc","materia","data_contratacao","sala")

    nome = fields.String(required=True)
    data_nasc = fields.Date(required=True)
    materia = fields.String(required=True)
    data_contratacao = fields.Date(required=True)
    sala = fields.String(required=True)
