from  datetime import date
from dataclasses import dataclass

@dataclass
class ProfessorDTO():
    nome: str
    data_nasc: date
    materia: str
    data_contratacao:date
    sala:str
    
