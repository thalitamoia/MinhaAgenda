import os
from flask import Flask, render_template,request
from models.model import db, Agenda
from controller.controller import lista_agenda, cria_contacto, atualiza_contactos,delete_contactos,pesquisar

app = Flask(__name__)

app.config['SECRET_KEY'] = 'TH072022'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'

db.init_app(app)

#rotas

app.add_url_rule('/', 'lista_agenda', lista_agenda)
app.add_url_rule('/cria_contacto', 'cria_contacto', cria_contacto, methods=['GET', 'POST'])
app.add_url_rule('/<int:id>/atualiza_contactos', 'atualiza_contactos', atualiza_contactos, methods=['GET','POST'])
app.add_url_rule('/<int:id>/delete_contactos','delete_contactos',delete_contactos)
app.add_url_rule('/pesquisar', 'pesquisar', pesquisar, methods=['GET','POST'])


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)