from flask import Blueprint, request, render_template, abort, redirect, url_for
from flask_datepicker import datepicker

from my_app.models import *
from my_app import db
from my_app.analisis import str_todf 

inicial = Blueprint('inicial',__name__)

@inicial.route('/', methods=['GET', 'POST'])
@inicial.route('/index')
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'Enviar Datos':
            linea = request.form['linea']
            
            fecha = request.form['fecha']
            fecha=datetime.strptime(fecha, '%d-%m-%Y')
            if request.form.get('hora_extra')==None:
                hora_extra=False
            else:
                hora_extra = True
            turno=request.form['fav_turno']
            dato= request.form['datos']
            
            #ingresa los datos de la tabla raw de respaldo
            data=data_raw(linea=linea, fecha= fecha, hora_extra=hora_extra, turno=turno, data=dato)
            db.session.add(data)
            
            #ingresa los datos divididos en asistencia y asistencia detalle el cual usa la funcion str_todf
            asist = asistencias(linea=linea, fecha=fecha, hora_extra=hora_extra, turno=turno) 
            db.session.add(asist)
            db.session.commit()
            id=asist.id_asistencia #obtiene el id de asistencia para ingresar el mismo el asistencia_detalle
            str_todf(dato, id)     #ingresa el dataframe de pandas en la base de datos
            db.session.close()
            
            print(id, linea, hora_extra, fecha,turno)
            return 'hecho' # do something
    
    return render_template('index.html')


@inicial.route('/test')
def test():
    #asist = asistencias(linea="gian", fecha="2021/09/15", hora_extra=True, turno=4) 
    #detalle=asistencia_detalle(id= asist, legajo=39642, dominio='prueba', puesto='p1', skill=1)
    data=data_raw(linea="anterior", fecha= datetime(2015, 6, 5), hora_extra=True, turno=1, data="ajdajdhjahdja, dajdhjahdj, hjahdj")
    db.session.add(data)
    db.session.commit()
    db.session.close()
    return "test"