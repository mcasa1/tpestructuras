from Conectores_BD import *
import math
import pandas as pd

# Clase para mantener una lista de Contactos
class ListaContactos:
    def __init__(self, nombre_lista_contacto, descripcion_lista_contacto,lista_contactos = [], fechaCreacion = None,ID_lista_contactos = None):
        self.ID_lista_contactos = ID_lista_contactos
        self.nombre_lista_contacto = nombre_lista_contacto
        self.descripcion_lista_contacto = descripcion_lista_contacto
        self.Contactos = lista_contactos
        self.fechaCreacion = fechaCreacion
    def __str__(self):
        return "ID: {}, Nombre: {}, Descripcion: {}, fecha de creacion: {}".format(self.ID_lista_contactos,self.nombre_lista_contacto, self.descripcion_lista_contacto, self.fechaCreacion)

class ListaContactosModel():
    def getListaContactosDatos(nombreListaContactos = None):
        #Conector
        MySql = Conectores_BD.conector_mysql()
                
        #Qwery
        qwery = "SELECT ID_LISTA_CONTACTOS, NOMBRE_LISTA_CONTACTOS, DESCRIPCION_LISTA_CONTACTOS, FECHA_CREACION FROM `LISTA_CONTACTOS`"

        if nombreListaContactos != None:
            optionalWhere = " WHERE NOMBRE_LISTA_CONTACTOS = '{}'".format(nombreListaContactos)
            qwery = qwery + optionalWhere

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
            result = conn.execute(text(qwery))
        return result
    def postListaContactos(lista_contactos):
        #Conector
        MySql = Conectores_BD.conector_mysql()
        
        #Qwery
        qwery = "INSERT INTO `LISTA_CONTACTOS` (`NOMBRE_LISTA_CONTACTOS`, `DESCRIPCION_LISTA_CONTACTOS`) VALUES ('{}','{}')".format(lista_contactos.nombre_lista_contacto, lista_contactos.descripcion_lista_contacto)

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
    def deleteListaContactos():
        pass
    def addContactos(df):
        #Conector
        MySql = Conectores_BD.conector_mysql()

        #CARGA DATOS A MYSQL
        tabla = 'CONTACTOS_LISTA_CONTACTOS'
        chunksz = math.floor((2100 / len(df.columns)))
        if (2100 % chunksz) == 0:
            chunksz = chunksz -1
            if chunksz > 1000:
                chunksz = 1000
        elif chunksz > 1000:
            chunksz = 1000
        
        df.to_sql(tabla, con = MySql, if_exists = 'append',index = False, method='multi', chunksize = chunksz)
    def getListaContactos_Contactos(nombreListaContactos = None):
        #Conector
        MySql = Conectores_BD.conector_mysql()
                
        #Qwery
        qwery = """SELECT
    LISTA_CONTACTOS.ID_LISTA_CONTACTOS,
    NOMBRE_LISTA_CONTACTOS,
    DESCRIPCION_LISTA_CONTACTOS,
    CONTACTOS.ID_CONTACTO,
    NOMBRE_CONTACTO,
    FECHA_NACIMIENTO,
    EMAIL,
    DIRECCION,
    SEXO
FROM CONTACTOS_LISTA_CONTACTOS
    INNER JOIN CONTACTOS ON
        CONTACTOS_LISTA_CONTACTOS.ID_CONTACTO = CONTACTOS.ID_CONTACTO
    INNER JOIN LISTA_CONTACTOS ON 
        CONTACTOS_LISTA_CONTACTOS.ID_LISTA_CONTACTOS = LISTA_CONTACTOS.ID_LISTA_CONTACTOS
WHERE CONTACTOS.CONTACTO_HABILITACION = 1;
        """

        if nombreListaContactos != None:
            optionalWhere = " AND NOMBRE_LISTA_CONTACTOS = '{}'".format(nombreListaContactos)
            qwery = qwery + optionalWhere

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
            result = conn.execute(text(qwery))
        return result


class ListaContactosController:
    def obtener_lista_contactos_contactos(nombreListaContactos = None) -> list:
        lista_contactos = []
        datos = ListaContactosModel.getListaContactos_Contactos()


        
        #for dato in datos:
        #    value = ListaContactos(dato[1], dato[2],fechaCreacion = dato[3],ID_lista_contactos = dato[0])
        #    lista_contactos.append(value)
        #return lista_contactos

    def crear_lista_contactos(nombre_lista_contacto, descripcion_lista_contacto):
        lista = ListaContactos(nombre_lista_contacto, descripcion_lista_contacto)
        ListaContactosModel.postListaContactos(lista)
    def agregarContactos(lista_contactos : ListaContactos):
        #crear un dataframe con los datos para enviar a SQL"
        df = pd.DataFrame()

        #crear una columna con cada valor de los atributos de los objetos de la lista de tiempo
        df['ID_CONTACTO'] = [x.ID_contacto for x in lista_contactos.Contactos]
        df['ID_LISTA_CONTACTOS'] = lista_contactos.Id_lista

        ListaContactosModel.addContactos(df)
    def obtener_lista_contactos_datos(nombreListaContactos = None) -> list:
        lista_contactos = []
        datos = ListaContactosModel.getListaContactosDatos(nombreListaContactos)
        for dato in datos:
            value = ListaContactos(dato[1], dato[2],fechaCreacion = dato[3],ID_lista_contactos = dato[0])
            lista_contactos.append(value)
        return lista_contactos



# TEST


# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
#ListaContactosController.crear_lista_contactos('+18/futbol','Lista con los contactos que les interesa el futbol y son mayores de edad')
#ListaContactosController.crear_lista_contactos('+18/futbol','Lista con los contactos que les interesa el futbol y son mayores de edad')
#ListaContactosController.crear_lista_contactos('+18/hockey','Lista con los contactos que les interesa el hockey y son mayores de edad')
#ListaContactosController.crear_lista_contactos('+18/volley','Lista con los contactos que les interesa el volley y son mayores de edad')
#ListaContactosController.crear_lista_contactos('+18/tenis','Lista con los contactos que les interesa el tenis y son mayores de edad')
#ListaContactosController.crear_lista_contactos('+18/handball','Lista con los contactos que les interesa el handball y son mayores de edad')
#ListaContactosController.crear_lista_contactos('+18/boxeo','Lista con los contactos que les interesa el boxeo y son mayores de edad')

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
#a = ListaContactosController.obtener_lista_contactos_datos('+18/futbol')
#for i in a:
#    print(i)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

ListaContactosController.obtener_lista_contactos_contactos()
