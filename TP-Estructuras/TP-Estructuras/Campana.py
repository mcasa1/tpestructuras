from Conectores_BD import *
from ListaContactos import *
from Mail import *
import array as array

# Clase Campana
class Campana(ListaContactos, Mail):
    def __init__(self, nombre_campana, descripcion, ID_lista_clientes, asunto):
        self.nombre_campana = nombre_campana
        self.descripcion = descripcion
        ListaContactos.__init__(self, ID_lista_clientes)
        Mail.__init__(self, asunto)

class CampanaController:

    campanas = [] 
        
    # Metodo para crear una campana
    def crear_campana(self, nombre_campana, descripcion, ID_lista_clientes, asunto):
        campana = Campana(nombre_campana, descripcion, ID_lista_clientes, asunto)
        Campana_model.Post_campana(campana)

    def obtener_campanas(nombre_campana = None) -> list:
        campanas = []
        datos = Campana_model.getCampanas(nombre_campana)
        for dato in datos:
            value = Campana(dato[0], dato[1],ID_lista_contactos = dato[2], asunto = dato[3])
            campanas.append(value)
        return campanas
        

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

    def getCampanas(nombre_campana = None):
        #Conector
        MySql = Conectores_BD.conector_mysql()
                
        #Qwery
        qwery = "SELECT nombre_campana, descripcion, LISTA_CLIENTES, MAIL FROM `CAMPANAS`"

        if nombre_campana != None:
            optionalWhere = " WHERE nombre_campana = '{}'".format(nombre_campana)
            qwery = qwery + optionalWhere

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
            result = conn.execute(text(qwery))
        return result
