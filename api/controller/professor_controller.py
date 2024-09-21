from flask_restful import Resource
from api import api
from ..schemas import professor_schema
from flask import request,make_response,jsonify
from ..dto import professor_dto
from ..service import professor_service
        
class ProfessorController(Resource):
    def get(self):
        professores = professor_service.lista_professores()
        validate = professor_schema.ProfessorSchema(many = True)
        return make_response(validate.jsonify(professores), 200)
    
    def post(self):
        professorSchema = professor_schema.ProfessorSchema()
        validate = professorSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            data_nasc = request.json["data_nasc"]
            materia = request.json["materia"]
            data_contratacao = request.json["data_contratacao"]
            sala = request.json["sala"]
            novo_professor = professor_dto.ProfessorDTO(nome = nome,data_nasc = data_nasc,materia = materia,data_contratacao = data_contratacao,sala = sala)
            retorno = professor_service.cadastrar_professor(novo_professor)
            professorJson = professorSchema.jsonify(retorno)
            return make_response(professorJson, 201)
    
    def put(self, id):
        professor = professor_service.listar_professor_id(id)
        if professor is None:
            return make_response(jsonify("Professor não encontrado"), 404)
        professorSchema = professor_schema.ProfessorSchema()
        validate = professorSchema.validate(request.json)
        if validate:
            make_response(jsonify(validate),400)
        else:
            nome = request.json["nome"]
            data_nasc = request.json["data_nasc"]
            materia = request.json["materia"]
            data_contratacao = request.json["data_contratacao"]
            sala = request.json["sala"]
            novoProfessorAlterado = professor_dto.ProfessorDTO(nome,data_nasc,materia,data_contratacao,sala)
            professor_service.atualizar_professor(professor, novoProfessorAlterado)
            professorAtualizado = professor_service.listar_professor_id(id)
            return make_response(professorSchema.jsonify(professorAtualizado), 200)
    
    def delete(self,id):
        professorBd = professor_service.listar_professor_id(id)
        if professorBd is None:
            return make_response(jsonify("Professor não encontrado"), 404)
        professor_service.excluir_professor(professorBd)
        return make_response(jsonify("Professor excluído com sucesso"), 200)
        

class ProfessorDetailController(Resource):
    def get(self,id):
        professor = professor_service.listar_professor_id(id)
        if professor is None:
            return make_response(jsonify("Professor não encontrado"), 404)
        validate = professor_schema.ProfessorSchema()
        return make_response(validate.jsonify(professor), 200)


api.add_resource(ProfessorController,'/professor')
api.add_resource(ProfessorController,'/professor/<int:id>', endpoint = 'Alterar Professor', methods = ["PUT"])
api.add_resource(ProfessorController,'/professor/<int:id>', endpoint = 'Excluir Professor', methods = ["DELETE"])
api.add_resource(ProfessorDetailController,'/professor/<int:id>')
    