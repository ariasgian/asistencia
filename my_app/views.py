from flask import Blueprint, request, render_template, abort, redirect, url_for
from flask_datepicker import datepicker
from sqlalchemy import text
import datetime



inicial = Blueprint('inicial',__name__)

#data = tabla_prog.query.all()

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
            print(linea, hora_extra, fecha,turno)
            return 'hecho' # do something
    
    return render_template('index.html')

@inicial.route('/test', methods=['GET', 'POST'])
@inicial.route('/test')
def test():
    
    return render_template('index2.html')