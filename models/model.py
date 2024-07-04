from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Agenda(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(50))
    telefone = db.Column(db.Integer)

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

