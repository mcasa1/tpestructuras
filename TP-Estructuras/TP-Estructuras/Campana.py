import re
import time
from Conectores_BD import *
from ListaContactos import *
from Mail import *
import array as array

# Clase Campana
class Campana(ListaContactos, Mail):
    def __init__(self, nombre_campana, descripcion, lista_clientes, mail):
        self.nombre_campana = nombre_campana
        self.descripcion = descripcion
        ListaContactos.__init__(self, lista_clientes)
        Mail.__init__(self, mail)

class CampanaController:

    campanas = [] 
        
    # Metodo para crear una campana
    def crear_campana(self, nombre_campana, descripcion, lista_clientes, mail):
        campana = Campana(nombre_campana, descripcion, lista_clientes, mail)
        Campana_model.Post_campana(campana)
        

class Campana_model: 
    def Post_campana(campana):
        #Conector
        MySql = Conectores_BD.conector_mysql()
        
        #Creo el cursor
        cnxn = MySql.raw_connection()
            
        #Qwery
        qwery = "INSERT INTO CAMPANAS (NOMBRE_CAMPANA, DESCRIPCION, LISTA_CLIENTES, MAIL) VALUES ('{}','{}','{}','{}')".format(campana.nombre, campana.descripcion, campana.lista_clientes, campana.mail)

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()