from my_app import db

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
    fecha = db.Column(db.String(50))
    hora_extra = db.Column(db.Integer) 
    turno = db.Column(db.String(50))
    
    
    def __init__(self, linea, fecha, hora_extra, turno):  
        self.linea = linea
        self.fecha = fecha
        self.hora_extra = hora_extra
        self.turno = turno
        
    

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
            
    # def __init__(self, id_a, legajo,dominio,puesto,skill):
    #     self.legajo = legajo
    #     self.id_asistencia=id_a
    #     self.dominio = dominio
    #     self.puesto = puesto
    #     self.skill = skill
        
