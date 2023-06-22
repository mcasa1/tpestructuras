from Conectores_BD import *
import math
import pandas as pd
from Contacto import *

class ListaContactos:
    def __init__(self, nombre_lista_contacto, descripcion_lista_contacto,lista_contactos = [], fechaCreacion = None,ID_lista_contactos = None):
        self.ID_lista_contactos = ID_lista_contactos
        self.nombre_lista_contacto = nombre_lista_contacto
        self.descripcion_lista_contacto = descripcion_lista_contacto
        self.Contactos = lista_contactos
        self.fechaCreacion = fechaCreacion
    def __str__(self):
        return "ID: {}, Nombre: {}, Descripcion: {}, fecha de creacion: {}".format(self.ID_lista_contactos,self.nombre_lista_contacto, self.descripcion_lista_contacto, self.fechaCreacion)

class ListaContactosController:
    def obtener_lista_contactos_contactos(nombreListaContactos = None) -> list:
        # Devuleve los datos generales de una lista de contactos. Nombre, descripcion y fecha de creacion Y devuelve datos de los contactos asignados en
        # Si no se especifica un nombre de ListaContatos, devuelve todos los datos que haya

        df = pd.DataFrame(ListaContactosModel.getListaContactos_Contactos())

        #crear un objeto Contacto con los valores de las columanas ID_CONTACTO,NOMBRE_CONTACTO, FECHA_NACIMIENTO, EMAIL, DIRECCION Y SEXO Y agregarlo en una nueva columna
        #del dataframe llamada Contacto
        df['Contacto'] = df.apply(lambda x: Contacto(id_contacto = x[3],nombre = x[4],fecha_nacimiento = x[5],email = x[6],direccion = x[7],sexo = x[8]), axis = 1)
        
        #conservar solo las columnas 'ID_LISTA_CONTACTOS','NOMBRE_LISTA_CONTACTOS','DESCRIPCION_LISTA_CONTACTOS','Contacto' del df
        df = df[['ID_LISTA_CONTACTOS','NOMBRE_LISTA_CONTACTOS','DESCRIPCION_LISTA_CONTACTOS','Contacto']]

        # agrupar las columnas por ID_LISTA_CONTACTOS, NOMBRE_LISTA_CONTACTOS, DESCRIPCION_LISTA_CONTACTOS y crear una lista con los valores de la columna Contacto
        df = df.groupby(['ID_LISTA_CONTACTOS','NOMBRE_LISTA_CONTACTOS','DESCRIPCION_LISTA_CONTACTOS'])['Contacto'].apply(list).reset_index(name='Contacto')

        #crear un objeto ListaContactos con los valores de las columanas ID_LISTA_CONTACTOS,NOMBRE_LISTA_CONTACTOS, DESCRIPCION_LISTA_CONTACTOS Y Contacto
        df['ListaContactos'] = df.apply(lambda x: ListaContactos(x[1],x[2],x[3],None,x[0]), axis = 1)

        #crear un objeto lista con los valores de la columna ListaContactos
        lista_contactos = df['ListaContactos'].tolist() 

        return lista_contactos
    def crear_lista_contactos(nombre_lista_contacto, descripcion_lista_contacto):
        #Crea una lista de contactos sin contactos asignados

        lista = ListaContactos(nombre_lista_contacto, descripcion_lista_contacto)
        brevo = Brevo_contactos()
        id_lista = brevo.post_lista_contactos(lista)
        lista.ID_lista_contactos = id_lista.id
        ListaContactosModel.postListaContactos(lista)
    def agregarContactos(lista_contactos : ListaContactos):
        #A partir de un objeto ListaContactos, agrega todos los contactos que esten en el atributo .Contactos []
        # a la tabla CONTACTOS_LISTA_CONTACTOS de la bd

        #crear un dataframe con los datos para enviar a SQL"
        df = pd.DataFrame()

        #crear una columna con cada valor de los atributos de los objetos de la lista de tiempo
        df['ID_CONTACTO'] = [x.ID_contacto for x in lista_contactos.Contactos]
        df['ID_LISTA_CONTACTOS'] = lista_contactos.Id_lista

        ListaContactosModel.addContactos(df)

        #llamar a la funcion post_contactos_form_lista_contactos de brevo en baches de 150 contactos
        #para no superar el limite de 150 contactos por llamada
        brevo = Brevo_contactos()
        for i in range(0,len(lista_contactos.Contactos),150):
            brevo.post_contactos_form_lista_contactos(lista_contactos.ID_lista_contactos, lista_contactos.Contactos[i:i+150])
    def obtener_lista_contactos_datos(nombreListaContactos = None) -> list:
        # Devuleve los datos generales de una lista de contactos. Nombre, descripcion y fecha de creacion. No devuelve datos de contactos
        # Si no se especifica un nombre de ListaContatos, devuelve todos. 

        lista_contactos = []
        datos = ListaContactosModel.getListaContactosDatos(nombreListaContactos)
        for dato in datos:
            value = ListaContactos(dato[1], dato[2],fechaCreacion = dato[3],ID_lista_contactos = dato[0])
            lista_contactos.append(value)
        return lista_contactos
    def eliminar_lista_contactos(id_lista_contactos):
        # Metodo para eliminar una Campaña
        brevo = Brevo_contactos()
        brevo.delete_lista_contactos(brevo,id_lista_contactos)
        ListaContactosModel.deleteListaContactos(id_lista_contactos)  

class ListaContactosModel():
    def getListaContactosDatos(nombreListaContactos = None):
        # Metodo para obtener los datos de cabecera de las listas. Permite obtener todos o uno en particular.

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
        # Metodo para agregar la cabecera de una lista de contactos.

        #Conector
        MySql = Conectores_BD.conector_mysql()
        
        #Qwery
        qwery = "INSERT INTO `LISTA_CONTACTOS` (`ID_LISTA_CONTACTOS`,`NOMBRE_LISTA_CONTACTOS`, `DESCRIPCION_LISTA_CONTACTOS`) VALUES ('{}','{}','{}')".format(lista_contactos.ID_lista_contactos,lista_contactos.nombre_lista_contacto, lista_contactos.descripcion_lista_contacto)

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
    def deleteListaContactos(id_lista_contactos):
        #Conector
        MySql = Conectores_BD.conector_mysql()
                
        #Qwerys para eliminar los contactos de la lista y despues eliminar los datos de cabecera
        qwery1 = "DELETE FROM CONTACTOS_LISTA_CONTACTOS WHERE ID_LISTA_CONTACTOS = 1".format(id_lista_contactos)
        qwery2 = "DELETE FROM LISTA_CONTACTOS WHERE ID_LISTA_CONTACTOS = 1".format(id_lista_contactos)
        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery1))
            conn.commit()
            conn.execute(text(qwery2))
            conn.commit()
    def addContactos(df):
        # Metodo para agregar los contactos a una lista de contactos.

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
        # Metodo para obtener los contactos de una lista de contactos. Permite obtener todas las listas o una en particular.

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
    def getListaContactos_atributos(id_atributo):
        

        MySql = Conectores_BD.conector_mysql()
                
        #Qwery
        qwery = """ SELECT ID_CONTACTO
                    FROM CONTACTOS
	                    INNER JOIN ATRIBUTOS_CONTACTOS ON 
    	                    CONTACTOS.ID_CONTACTO = ATRIBUTOS_CONTACTOS.ID_CONTACTO
                    WHERE ATRIBUTOS_CONTACTOS.ID_ATRIBUTO = {}'""".format(id_atributo)

         #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
            result = conn.execute(text(qwery))
        return result
