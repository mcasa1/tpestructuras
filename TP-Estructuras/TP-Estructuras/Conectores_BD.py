import pandas as pd
from sqlalchemy import create_engine, text
from credenciales import *
class Conectores_BD:
 
    #MySql CotyApp -- MySql CotyApp -- MySql CotyApp
    
    def conector_mysql():
        user= credenciales.sql.get('user')
        password=credenciales.sql.get('password')
        server = credenciales.sql.get('server')
        database = credenciales.sql.get('database')
        cnxn = create_engine('mysql+pymysql://'+ user +':'+ password +'@'+ server +'/'+ database)   
        return cnxn
    
# dejo 3 metodos para llamar a la BD
# 1) Consulta: devuelve un dataframe
# 2) Ejecutar: ejecuta una query y devuelve la cantidad de filas afectadas
# 3) Query_un_valor: devuelve un unico valor (el primero de la primera fila)

#se puede hacer un: MySql.connect().execute(text(qwery)) y no transformarlo al type DATAFRAME, pero en ese caso
#devuelve un objeto del tipo SQLALCHEMY que es la libreria para hacer las conexiones
#es un objeto iterable y se puede indicar por indice o nombre a la columna que se hace referencia de los resultados de la consulta
# dejo esos metodos porque creo que son los formatos que mas podemos usar.



    def consultar_MySql(qwery):
        MySql = Conectores_BD.conector_mysql()
        df = pd.DataFrame(MySql.connect().execute(text(qwery)))
        return df
    
    def ejecutar_MySql(qwery):
        #Conector
        MySql = Conectores_BD.conector_mysql()
        
        #Creo el cursor
        cnxn = MySql.raw_connection()
         
        #Ejecuto el comando y guardo cambios
        with cnxn.cursor() as cursor:
            cursor.execute(qwery)
            cnxn.commit()
        
        return cursor.rowcount

    def Query_un_valor(sql):
        Engine =  Conectores_BD.conector_mysql()
        result = Engine.connect().execute(text(sql))
        return result.fetchone()[0]