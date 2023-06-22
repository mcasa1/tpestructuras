from Conectores_BD import *

class Atributo:
    def __init__(self, AtributoDescripcion, ID_atributo=None):
        self.ID_atributo = ID_atributo
        self.AtributoDescripcion = AtributoDescripcion

    def __str__(self):
        return "ID: {}, descripcion: {}".format(self.ID_atributo, self.AtributoDescripcion)
class AtributosController:

    ListaAtributos = []

    def agregar_atributo(AtributoDescripcion):
        # Metodo para agregar un atributo

        atributo = Atributo(AtributoDescripcion)
        Atributos_Model.Post_atributo(atributo)
    def eliminar_atributo(nombre_atributo):
        # Metodo para eliminar un atributo
        Atributos_Model.Delete_atributo(nombre_atributo)
    def obtener_atributos():
        # obtener todos los atributos

        lista_atributos = []
        datos = Atributos_Model.Listar_atributos()
        for dato in datos:
            atributo = Atributo(dato[1], dato[0])
            lista_atributos.append(atributo)
        return lista_atributos
class Atributos_Model:
    def Post_atributo(atributo):
        #Conector
        MySql = Conectores_BD.conector_mysql()
        
        #Creo el cursor
        cnxn = MySql.raw_connection()
         
        #Qwery
        qwery = "INSERT INTO ATRIBUTOS (ATRIBUTO_DESCRIPCION) VALUES ('{}')".format(atributo.AtributoDescripcion)

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
    def Listar_atributos():
        #Conector
        MySql = Conectores_BD.conector_mysql()
                
        #Qwery
        qwery = "SELECT ID_ATRIBUTO, ATRIBUTO_DESCRIPCION FROM ATRIBUTOS"

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
            result = conn.execute(text(qwery))
        return result
    def Delete_atributo(atributo):
        #Conector
        MySql = Conectores_BD.conector_mysql()
                
        #Qwery
        qwery = "DELETE FROM ATRIBUTOS WHERE ATRIBUTO_DESCRIPCION = '{}'".format(atributo)

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()