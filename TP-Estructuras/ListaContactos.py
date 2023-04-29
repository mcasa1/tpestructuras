from Conectores_BD import *
import math

# Clase para mantener una lista de Contactos
class ListaContactos:
    def __init__(self, nombre_lista_contacto, descripcion_lista_contacto, lista_contactos = [], ID_lista_contactos = None):
        self.ID_lista_contactos = ID_lista_contactos
        self.nombre_lista_contacto = nombre_lista_contacto
        self.descripcion_lista_contacto = descripcion_lista_contacto
        self.Contactos = lista_contactos





class ListaContactosModel():
    def getListaContactos():
        pass
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
        
        df.to_sql(tabla, con = MySql, if_exists = 'append' ,index = False, method='multi', chunksize = chunksz)

class ListaContactosController:
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