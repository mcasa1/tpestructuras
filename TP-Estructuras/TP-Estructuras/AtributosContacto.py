from Conectores_BD import *
from Atributos import *
from Contacto import *


class Atributos_Contacto(Atributo,Contacto):
    def __init__(self, ID_Atributo, id):
        Atributo.__init__(self, ID_Atributo)
        Contacto.__init__(self, id)
        
class Atributos_Contacto_Controller():

    Lista_Atributos = []

    #Metodo para vincular atributos a un contacto
    def vincular_atributos_contacto(ID_Atributo, id):
        atributos_contacto = Atributos_Contacto(ID_Atributo, id)
        Atributos_Contacto_Model.Post_atributos_contacto(atributos_contacto)


class Atributos_Contacto_Model():
    
    def Post_atributos_contacto(atributos_contacto):
        #Conector
        MySql = Conectores_BD.conector_mysql()
        
        #Creo el cursor
        cnxn = MySql.raw_connection()
            
        #Qwery
        qwery = "INSERT INTO ATRIBUTOS_CONTACTO (ID_ATRIBUTO, ID_CONTACTO) VALUES ('{}','{}')".format(atributos_contacto.ID_Atributo, atributos_contacto.id)

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()