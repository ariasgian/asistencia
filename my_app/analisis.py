import pandas as pd
import io


def convertir(texto):
    lineas=texto.split('\n')
    for linea in lineas:
        puesto=linea[2]
        dominio=linea[3]
        skill= linea[4]
        legajo= linea[5]
    return puesto, dominio, skill, legajo





def conv(texto):
    name=['puesto', 'dominio', 'skill', 'legajo']
    df= pd.read_csv(texto, sep=',', usecols=[2,3,4,5], names=name)
    return df
    
text_file=open('data.txt')
#read whole file to a string
data_string = text_file.read()
 
#close file
text_file.close()
 
data = io.StringIO(data_string)
df= conv(data)
#linea, dominio, skill, lehgajo=convertir("1,Anterior,Rack 01,Premontaje,SKILL 1,41094")