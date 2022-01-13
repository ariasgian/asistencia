import pandas as pd
import io
from sqlalchemy import create_engine


def convertir(texto):
    lineas=texto.split('\n')
    for linea in lineas:
        puesto=linea[2]
        dominio=linea[3]
        skill= linea[4]
        legajo= linea[5]
    return puesto, dominio, skill, legajo

def str_todf(data_string):
    texto=io.StringIO(data_string)
    df= pd.read_csv(texto, sep=',', usecols=[2,3,4,5], names=name)
    return df
    
db = create_engine('sqlite:///database.db')

data_raw="""1,Anterior,Rack 01,Premontaje,SKILL 1,41094
2,Anterior,Rack 02,Premontaje,SKILL 1,41612"""

df= str_todf(data_raw)
df.to_sql('asistencia', db, if_exists='append')

