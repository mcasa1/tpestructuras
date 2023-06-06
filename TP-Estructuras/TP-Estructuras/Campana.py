import re
import time
from datetime import datetime
from Conectores_BD import *
from ListaContactos import *
import array as array

# Clase Campana
class Campana(ListaContactos):
    def __init__(self, nombre_campana, descripcion, fecha, ID_lista_clientes, id_mail):
        self.nombre_campana = nombre_campana
        self.descripcion = descripcion
        self.fecha = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
        ListaContactos.__init__(self, ID_lista_clientes)
        self.id_mail = id_mail

class CampanaController:

    campanas = [] 
        
    # Metodo para crear una campana
    def crear_campana(self, nombre_campana, descripcion, fecha, ID_lista_clientes, id_mail):
        campana = Campana(nombre_campana, descripcion, fecha, ID_lista_clientes, id_mail)
        Campana_model.Post_campana(campana)

    def obtener_campanas(nombre_campana = None) -> list:
        campanas = []
        datos = Campana_model.getCampanas(nombre_campana)
        for dato in datos:
            value = Campana(dato[0], dato[1], fecha = dato[2], ID_lista_contactos = dato[3], id_mail = dato[4])
            campanas.append(value)
        return campanas
        

class Campana_model: 
    def Post_campana(campana):
        #Conector
        MySql = Conectores_BD.conector_mysql()
        
        #Creo el cursor
        cnxn = MySql.raw_connection()
            
        #Qwery
        qwery = "INSERT INTO CAMPAÑAS (NOMBRE_CAMPAÑA, DESCRIPCION_CAMPAÑA, FECHA_ENVIO, ID_LISTA_CONTACTOS, ID_MAIL) VALUES ('{}','{}','{}','{}','{}')".format(campana.nombre, campana.descripcion, campana.fecha, campana.lista_clientes, campana.id_mail)

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()

    def getCampanas(nombre_campana = None):
        #Conector
        MySql = Conectores_BD.conector_mysql()
                
        #Qwery
        qwery = "SELECT NOMBRE_CAMPAÑA, DESCRIPCION_CAMPAÑA, FECHA_ENVIO, ID_LISTA_CONTACTOS, ID_MAIL FROM `CAMPAÑAS`"

        if nombre_campana != None:
            optionalWhere = " WHERE NOMBRE_CAMPAÑA = '{}'".format(nombre_campana)
            qwery = qwery + optionalWhere

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
            result = conn.execute(text(qwery))
        return result
