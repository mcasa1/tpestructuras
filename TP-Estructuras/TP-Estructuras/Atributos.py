from Conectores_BD import *

#Clase de atributos
class Atributo:
    def __init__(self, AtributoDescripcion, ID_atributo=None):
        self.ID_atributo = ID_atributo
        self.AtributoDescripcion = AtributoDescripcion

# Clase para manejar los atributos
class AtributosController:

    ListaAtributos = []

    # Metodo para agregar un atributo
    def agregar_atributo(AtributoDescripcion):
        atributo = Atributo(AtributoDescripcion)
        Atributos_Model.Post_atributo(atributo)

    # obtener todos los atributos
    def obtener_atributos():
        lista_atributos = []
        datos = Atributos_Model.Listar_atributos()
        for dato in datos:
            atributo = Atributo(dato[1], dato[0])
            lista_atributos.append(atributo)
        return lista_atributos

    ## Metodo para eliminar un atributo
    #def eliminar_atributo(self, nombre):
    #    for atributo in self.atributos:
    #        if atributo.nombre == nombre:
    #            self.atributos.remove(atributo)
    #            print(f"Atributo {atributo.nombre} eliminado")
    #            break
    #    else:
    #        print("No se encontro el atributo")

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
  
            
# TEST DE METODOS

#AtributosController.agregar_atributo('SS')
