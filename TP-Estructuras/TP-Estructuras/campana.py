from Conectores_BD import *
from ListaContactos import *
import array as array
from Brevo import Brevo_campañas

# Clase Campaña
class Campaña(ListaContactos):
    def __init__(self,nombre_campaña, descripcion_campaña,fecha_envio,ID_lista_contactos,id_mail,id_campaña=None):
        self.id_campaña = id_campaña
        self.nombre_campaña = nombre_campaña
        self.descripcion_campaña = descripcion_campaña
        self.fecha_envio = fecha_envio
        self.ID_lista_contactos = ID_lista_contactos
        #ListaContactos.__init__(self, ID_lista_contactos)
        self.id_mail = id_mail

class CampañaController:
    campañas = [] 
    # Metodo para crear una Campaña
    def crear_campaña(nuevaCampaña : Campaña):
        brevo = Brevo_campañas()
        response = brevo.post_campaña(nuevaCampaña)
        nuevaCampaña.id_campaña = response.id
        Campaña_model.Post_campaña(nuevaCampaña)

    def obtener_campañas(nombre_campaña = None) -> list:
        campañas = []
        datos = Campaña_model.getCampañas(nombre_campaña)
        for dato in datos:
            value = Campaña(id_campaña=dato[0], nombre_campaña= dato[1],descripcion_campaña=dato[2],fecha_envio=dato[3],ID_lista_contactos=dato[4],id_mail=dato[5])
            campañas.append(value)
        return campañas
        
class Campaña_model: 
    def Post_campaña(Campaña:Campaña):
        #Conector
        MySql = Conectores_BD.conector_mysql()
        
        #Creo el cursor
        cnxn = MySql.raw_connection()
            
        #Qwery
        qwery = """INSERT INTO `CAMPAÑAS` 
                        (`ID_CAMPAÑA`, `NOMBRE_CAMPAÑA`, `DESCRIPCION_CAMPAÑA`, `FECHA_ENVIO`, `ID_LISTA_CONTACTOS`, `ID_MAIL`, `FECHA_CREACION`)
                   VALUES 
                        ({},'{}','{}','{}','{}','{}',current_timestamp())""".format(Campaña.id_campaña, Campaña.nombre_campaña, Campaña.descripcion_campaña, Campaña.fecha_envio, Campaña.ID_lista_contactos, Campaña.id_mail)

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
    def getCampañas(nombre_campaña = None):
        #Conector
        MySql = Conectores_BD.conector_mysql()
                
        #Qwery
        qwery = """SELECT 
                        ID_CAMPAÑA,
                        NOMBRE_CAMPAÑA,
                        DESCRIPCION_CAMPAÑA,
                        FECHA_ENVIO,
                        NOMBRE_LISTA_CONTACTOS,
                        ID_MAIL 
                    FROM CAMPAÑAS
                        INNER JOIN LISTA_CONTACTOS ON 
                            CAMPAÑAS.ID_LISTA_CONTACTOS = LISTA_CONTACTOS.ID_LISTA_CONTACTOS"""

        if nombre_campaña != None:
            optionalWhere = " WHERE nombre_campana = '{}'".format(nombre_campaña)
            qwery = qwery + optionalWhere

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
            result = conn.execute(text(qwery))
        return result

#c = Campaña('prueba 1', 'prueba 1', '2023-06-19 20:00:00',2,2)
#CampañaController.crear_campaña(c)