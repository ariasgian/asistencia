from my_app import db
from datetime import datetime

class tbl_asistencia(db.Model):
    __tablename__= 'asistencia'
    id_asistencia = db.Column(db.Integer, primary_key=True)
    linea = db.Column(db.String(50))
    fecha = db.Column(db.String(50))
    hora_extra = db.Column(db.Integer) 
    turno = db.Column(db.String(50))
    

    def __init__(self, linea, fecha, hora_extra, turno):
        
        self.linea = linea
        self.fecha = fecha
        self.hora_extra = hora_extra
        self.turno = turno
        
    

