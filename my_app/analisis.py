import pandas as pd
import io
from my_app import db

def str_todf(data_string, id_asistencia):
    texto=io.StringIO(data_string)
    name=['puesto', 'dominio', 'skill', 'legajo']
    df= pd.read_csv(texto, sep=',', usecols=[2,3,4,5], names=name)
    df['id_asistencia']=id_asistencia
    df[['text','skill']] = df['skill'].str.split(' ',expand=True)
    df['skill']= df['skill'].astype(int)
    df.drop('text', axis=1, inplace=True)
    df.to_sql('asistencia_detalle', db.engine, if_exists='append', index=False)
    return 0
    
# db = create_engine('sqlite:///database.db')

# data_raw="""1,Anterior,Rack 01,Premontaje,SKILL 1,41094
# 2,Anterior,Rack 02,Premontaje,SKILL 1,41612
# 3,Anterior,Rack 03,Premontaje,SKILL 1,41231
# 4,Anterior,Rack 04,Premontaje,SKILL 1,41010
# 5,Anterior,Rack 05,Premontaje,SKILL 1,41582"""

# df= str_todf(data_raw)
# df['id_asistencia']=1
# df[['text','skill']] = df['skill'].str.split(' ',expand=True)
# df['skill']= df['skill'].astype(int)
# df.drop('text', axis=1, inplace=True)
# #%%
#df.to_sql('asistencia_detalle', db, if_exists='append', index=False)

