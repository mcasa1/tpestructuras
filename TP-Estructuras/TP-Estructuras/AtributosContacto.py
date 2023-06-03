from Conectores_BD import *
from Atributos import *
from Contacto import *


class Atributos_Contacto():
    def __init__(self, atributo:Atributo, contacto:Contacto):
        self.ID_atributo = atributo.ID_atributo
        self.id = contacto.id
        
        
class Atributos_Contacto_Controller():

    #Metodo para vincular atributos a un contacto
    def __init__(self, atributo, contacto):
        self.ac = Atributos_Contacto(atributo, contacto)
        
    def vincular_atributos_contacto(self):
        Atributos_Contacto_Model.Post_atributos_contacto(self.ac)
        
    def __str__(self):
        return "ID_atributo: {}, id: {}".format(self.ac.ID_atributo, self.ac.id)


class Atributos_Contacto_Model():
    
    def Post_atributos_contacto(atributos_contacto:Atributos_Contacto):
        #Conector
        MySql = Conectores_BD.conector_mysql()
        
        #Creo el cursor
        cnxn = MySql.raw_connection()
            
        #Qwery
        qwery = "INSERT INTO ATRIBUTOS_CONTACTO (ID_ATRIBUTO, ID_CONTACTO) VALUES ('{}','{}')".format(atributos_contacto.ID_atributo, atributos_contacto.id)

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
             

atributo = Atributo("futbol", 433434)
contacto = Contacto("roman", "roman@bc.com","02/02/2022", "Melian 123", "F", 232432432)

a = Atributos_Contacto_Controller(atributo, contacto)
a.vincular_atributos_contacto()