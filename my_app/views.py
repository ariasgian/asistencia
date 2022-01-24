from flask import Blueprint, request, render_template, abort, redirect, url_for
#from flask_datepicker import datepicker
from my_app.models import *
from my_app import db
from my_app.analisis import str_todf 
from my_app.reques import sendResJson
from datetime import datetime

def dataToJson(dato: asistencias):
    return {
        'linea' : dato.linea,
        'turno' : dato.turno,
        'fecha' : datetime.strftime(dato.fecha,'%d/%m/%Y'),
        'hora_extra': dato.hora_extra,
        'legajo': dato.legajo,
        'dominio': dato.dominio,
        'puesto': dato.puesto,
        'skill': dato.skill
        
    }

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
    data=data_raw(linea="anterior", fecha= datetime(2015, 6, 5), hora_extra=True, turno=1, data="ajdajdhjahdja, dajdhjahdj, hjahdj")
    db.session.add(data)
    db.session.commit()
    db.session.close()
    return "test"

@inicial.route('/data')
def data():
    query="""Select linea, fecha, turno, hora_extra, legajo, dominio, puesto, skill from asistencia 
    join asistencia_detalle on asistencia.id_asistencia = asistencia_detalle.id_asistencia"""
    
    respuesta=db.engine.execute(query)
    db.session.close()
    res= [] #se genera array vacio para agregar json
    for dato in respuesta:
        print(dato)
        res.append(dataToJson(dato))
        print(dataToJson(dato))
    return sendResJson(res,None, 200) #el json genera forma de dict 
    print(res)