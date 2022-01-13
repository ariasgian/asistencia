from flask import Blueprint, request, render_template, abort, redirect, url_for
from flask_datepicker import datepicker

from my_app.models import asistencias, asistencia_detalle
from my_app import db

inicial = Blueprint('inicial',__name__)

@inicial.route('/', methods=['GET', 'POST'])
@inicial.route('/index')
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'Enviar Datos':
            linea = request.form['linea']
            
            fecha = request.form['fecha']
            if request.form.get('hora_extra')==None:
                hora_extra=0
            else:
                hora_extra = request.form['hora_extra']
            turno=request.form['fav_turno']
            dato= request.form['datos']
            p=tbl_asistencia(linea, fecha, hora_extra, turno)
            db.session.add(p)
            db.session.commit()
            db.session.close()
            print(linea, hora_extra, fecha,turno)
            return 'hecho' # do something
    
    return render_template('index.html')


@inicial.route('/test')
def test():
    asist = asistencias("gian", "fecha12", 1, 4)
    #db.session.add(asist)
    #db.session.flush()
    detalle=asistencia_detalle(id= asist, legajo=39642, dominio='prueba', puesto='p1', skill=1)
    db.session.add(detalle)
    db.session.commit()
    db.session.close()
    return "test"