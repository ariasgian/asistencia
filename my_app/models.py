from my_app import db
from datetime import datetime


class asistencias(db.Model):
    """
    linea= strings,
    fecha= strings,
    Hora_extra= 1 o 0,
    turno= string(50),
    """
    __tablename__= 'asistencia'
    id_asistencia = db.Column(db.Integer, primary_key=True)
    linea = db.Column(db.String(50))
    fecha = db.Column(db.DateTime)
    hora_extra = db.Column(db.Boolean) 
    turno = db.Column(db.Integer)
class asistencia_detalle(db.Model):
    """
    legajo= integer,
    dominio= string(50),
    puesto= string(50),
    skill=integer
    """
    __tablename__= 'asistencia_detalle'
    id_as_detalle = db.Column(db.Integer, primary_key=True)
    id_asistencia = db.Column(db.Integer, db.ForeignKey('asistencia.id_asistencia'), nullable=False)
    legajo = db.Column(db.Integer)
    dominio = db.Column(db.String(50)) 
    puesto = db.Column(db.String(50))
    skill =db.Column(db.Integer)
    id = db.relationship('asistencias', backref = 'asistencia_detalle')
            
class data_raw(db.Model):
    id_data= db.Column(db.Integer, primary_key = True)
    linea = db.Column(db.String(50))
    fecha = db.Column(db.DateTime)
    hora_extra = db.Column(db.Boolean) 
    turno = db.Column(db.Integer)
    data = db.Column(db.Text())
      
#db.create_all()      
