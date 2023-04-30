import re
import time
from Conectores_BD import *


# Clase contacto
class Contacto:
    def __init__(self, nombre=None, email=None, fecha_nacimiento=None, direccion=None, sexo=None, id=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.sexo = sexo
        self.oculto = 1
    

    def validar_nombre(nombre: str) -> bool:
        if nombre.isalpha():
            return True
        else:
            return False

    def validar_email(email: str) -> bool:
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
            return True
        else:  
            return False 

    def validar_fecha_nacimiento(fecha_nacimiento: str) -> bool:
        try:
            fecha_valida = time.strptime(fecha_nacimiento, "%Y/%m/%d")
            return True
        except:
            return False

    def validar_direccion(direccion: str) -> bool:
        direccion_lista = direccion.split(" ")
        if len(direccion_lista) == 2:
            if direccion_lista[0].isalpha() and direccion_lista[1].isnumeric():
                return True
            else:
                return False

    def validar_sexo(sexo: int) -> bool:
        if sexo in [0,1]:
            return True
        else:
            return False

    validar_dicc = {"nombre": validar_nombre,
                    "email": validar_email,
                    "fecha_nacimiento": validar_fecha_nacimiento,
                    "direccion": validar_direccion,
                    "sexo": validar_sexo}

    def validar(self, key: str, data: str) -> bool:
        return self.validar_dicc[key](data)


# Clase para manejar los contactos
class Contacto_Controller:

    contactos = []

    # Metodo para agregar un contacto con id unico
    def agregar_contacto(nombre, email, fecha_nacimiento, direccion, sexo):
        contacto = Contacto(nombre, email, fecha_nacimiento, direccion, sexo)
        Contacto_Model.Post_contacto(contacto)
    
    # Metodo para imprimir los contactos no ocultos con parametro
    def obtener_contactos(id, nombre, email, fecha_nacimiento, direccion, sexo):
        contacto = Contacto(id, nombre, email, fecha_nacimiento, direccion, sexo)
        datos = Contacto_Model.listar_contactos(contacto)
        if contacto.oculto != 0:
            for dato in datos:
                contacto_devuelto = Contacto(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])
                contactos = contactos.append(contacto_devuelto)
        return contactos
    
    # Metodo para imprimir todos los contactos
    def obtener_contactos_todos():
        contactos_todos = []
        datos = Contacto_Model.listar_contactos_todos()
        for dato in datos:
            contacto = Contacto(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])
            contacto = contactos_todos.append(contacto)
        return contactos_todos

    # Metodo para ocultar un contacto
    def ocultar_contacto_control(email):
        contacto = Contacto()
        contacto.email = email
        Contacto_Model.ocultar_contacto(contacto)


class Contacto_Model:
    
    def Post_contacto(contacto):
        #Conector
        MySql = Conectores_BD.conector_mysql()
        
        #Creo el cursor
        cnxn = MySql.raw_connection()
            
        #Qwery
        qwery = "INSERT INTO CONTACTOS (NOMBRE_CONTACTO, FECHA_NACIMIENTO, EMAIL, DIRECCION, SEXO) VALUES ('{}','{}','{}','{}','{}')".format(contacto.nombre, contacto.fecha_nacimiento, contacto.email, contacto.direccion, contacto.sexo)

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()

    def listar_contactos(contacto, edaddesde, edadhasta):
        #Conector
        MySql = Conectores_BD.conector_mysql()
                
        #Qwery
        qwery = "SELECT ID_CONTACTO, NOMBRE_CONTACTO, FECHA_NACIMIENTO, EMAIL, DIRECCION, SEXO FROM CONTACTOS INNER JOIN ATRIBUTOS_CONTACTO WHERE ID = '{}' OR NOMBRE_CONTACTO = '{}' OR FECHA_NACIMIENTO = '{}' OR EMAIL = '{}' OR DIRECCION = '{}' OR SEXO = '{}'".format(contacto.id, contacto.nombre, contacto.fecha_nacimiento, contacto.email, contacto.direccion, contacto.sexo)
        
        if contacto.id != None or contacto.nombre!= None or contacto.fecha_nacimiento != None or contacto.email != None or contacto.direccion != None or contacto.sexo or edad != None:
            qwery = qwery + "WHERE"
        
        if contacto.id != None:
            optionalwhere = "NOMBRE_CONTACTO = '{}' AND".format(contacto.nombre)
            qwery = qwery + optionalwhere
            
        if contacto.nombre != None:
            optionalwhere = "NOMBRE_CONTACTO = '{}' AND".format(contacto.nombre)
            qwery = qwery + optionalwhere
        
        if contacto.fecha_nacimiento != None:
            optionalwhere = "FECHA_NACIMIENTO = '{}' AND".format(contacto.fecha_nacimiento)
            qwery = qwery + optionalwhere
        
        if contacto.email != None:
            optionalwhere = "EMAIL = '{}' AND".format(contacto.email)
            qwery = qwery + optionalwhere
        
        if contacto.direccion != None:
            optionalwhere = "DIRECCION = '{}' AND".format(contacto.direccion)
            qwery = qwery + optionalwhere
        
        if contacto.sexo != None:
            optioanlwhere = "SEXO = '{}' AND".format(contacto.sexo)
            qwery = qwery + optionalwhere
        
        if edaddesde != None and edadhasta != None:
            optionalwhere = "(SELECT DATEDIFF(CURDATE() ,FECHA_NACIMIENTO)) BETWEEN '{}' AND '{}' AND".format(edaddesde, edadhasta)
            qwery = qwery + optionalwhere
            
        
        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
            result = conn.execute(text(qwery))
        return result

    def listar_contactos_todos():
        #Conector
        MySql = Conectores_BD.conector_mysql()
                
        #Qwery
        qwery = "SELECT ID_CONTACTO, NOMBRE_CONTACTO, FECHA_NACIMIENTO, EMAIL, DIRECCION, SEXO FROM CONTACTOS"
        
        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
            result = conn.execute(text(qwery))
        return result


    def ocultar_contacto(contacto):
        #Conector
        MySql = Conectores_BD.conector_mysql()
        
        #Qwery
        qwery = "UPDATE CONTACTOS SET CONTACTO_HABILITACION = 0 WHERE EMAIL = '{}'".format(contacto.email)
        
        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()

Contacto_Controller.agregar_contacto("Lucas", "lucas@gmail.com", "1234/02/12", "remo 123", 0)

# Contacto_Controller.ocultar_contacto_control("tomas@gmail.com")

# Contacto_Controller.obtener_contactos_todos()
