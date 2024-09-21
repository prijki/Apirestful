from ..models import professor_model
from api import db

def cadastrar_professor(professor):
    professor_bd = professor_model.Professor(nome = professor.nome,
                                            data_nasc = professor.data_nasc,
                                            materia = professor.materia, 
                                            data_contratacao = professor.data_contratacao,
                                            sala = professor.sala)
    db.session.add(professor_bd)
    db.session.commit()
    return professor_bd

def lista_professores():
    professores = professor_model.Professor.query.all()
    return professores

def listar_professor_id(parm_id):
    professor = professor_model.Professor.query.filter_by(id=parm_id).first()
    return professor

def atualizar_professor(professor_bd,professor_atualizado):
    professor_bd.nome = professor_atualizado.nome
    professor_bd.data_nasc = professor_atualizado.data_nasc
    professor_bd.materia = professor_atualizado.materia
    professor_bd.data_contratacao = professor_atualizado.data_contratacao
    professor_bd.sala = professor_atualizado.sala
    db.session.commit()

def excluir_professor(professor):
    db.session.delete(professor)
    db.session.commit()