from flask import render_template, request, redirect, session, url_for, flash
from models.model import db, Agenda

def lista_agenda():
    return render_template('agenda.html', agenda = Agenda.query.all())


def cria_contacto():
    nome = request.form.get('nome')
    contacto = request.form.get('contacto')
    
    if request.method == 'POST': 
        if not nome or not contacto:
            flash('Preencha todos os campos', 'error')
        else:    
            agenda = Agenda(nome, contacto)
            db.session.add(agenda)
            db.session.commit()
            return redirect(url_for('lista_agenda'))


    return render_template('novo_contacto.html')

def atualiza_contactos(id):
    agenda = Agenda.query.filter_by(id=id).first()
    if request.method == 'POST':
        nome = request.form.get('nome')
        contacto = request.form.get('contacto')
        Agenda.query.filter_by(id=id).update({'nome':nome, 'telefone':contacto})
        db.session.commit()
        return redirect(url_for('lista_agenda'))
    return render_template('atualiza_contactos.html', agenda=agenda)

def delete_contactos(id):
    agenda = Agenda.query.filter_by(id=id).first()
    db.session.delete(agenda)
    db.session.commit()
    return redirect(url_for('lista_agenda'))

def pesquisar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        resultados = Agenda.query.filter(Agenda.nome.ilike(f'%{nome}%')).all()
        return render_template('pesquisar.html', resultados=resultados)
