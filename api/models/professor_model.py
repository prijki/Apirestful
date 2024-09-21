from api import db

class Professor(db.Model):
    __tablename__ = "Professor"
    id = db.Column(db.Integer,primary_key=True, autoincrement=True,nullable = False)
    nome = db.Column(db.String(100),nullable = False)
    data_nasc = db.Column(db.Date,nullable = False)
    materia = db.Column(db.String(100),nullable = False)
    data_contratacao = db.Column(db.Date,nullable = False)
    sala = db.Column(db.String(100),nullable = False)
    
