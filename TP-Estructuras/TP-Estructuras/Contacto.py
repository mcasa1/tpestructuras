import re
import time
from Conectores_BD import *
from Atributos import *
import array as array
from Brevo import *
from TP_Estructuras import ContactosMenu

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
    def __str__(self):
        return "ID: {}, Nombre: {}, Email: {}, Fecha de nacimiento: {}, Direccion: {}, Sexo: {}".format(self.id, self.nombre, self.email, self.fecha_nacimiento, self.direccion, self.sexo)
    

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
        brevo = Brevo()
        id_contacto = brevo.post_contacto(contacto)
        contacto.id = id_contacto
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
        qwery = "INSERT INTO CONTACTOS (ID_CONTACTO, NOMBRE_CONTACTO, FECHA_NACIMIENTO, EMAIL, DIRECCION, SEXO) VALUES ('{}','{}','{}','{}','{}','{}')".format(contacto.id,contacto.nombre, contacto.fecha_nacimiento, contacto.email, contacto.direccion, contacto.sexo)

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()

    def listar_contactos(contacto, edaddesde, edadhasta, atributo):
        atributo = Atributo()
        #Conector
        MySql = Conectores_BD.conector_mysql()
                
        #Qwery
        qwery = "SELECT ID_CONTACTO, NOMBRE_CONTACTO, FECHA_NACIMIENTO, EMAIL, DIRECCION, SEXO FROM CONTACTOS LEFT JOIN ATRIBUTOS_CONTACTO"
        
        qa = array("b", [0,0,0,0,0,0,0,0])
        
        if contacto.id != None:
            qa.insert(0,1)
        if contacto.nombre != None:
            qa.insert(1,1)
        if contacto.fecha_nacimiento != None:
            qa.insert(2,1)
        if contacto.email != None:
            qa.insert(3,1)
        if contacto.direccion != None:
            qa.insert(4,1)
        if contacto.sexo != None:
            qa.insert(5,1)
        if edaddesde and edadhasta!= None:
            qa.insert(6,1)
        if atributo.ID_atributo != None:
            qa.insert(7,1)
        
        if contacto.id != None or contacto.nombre!= None or contacto.fecha_nacimiento != None or contacto.email != None or contacto.direccion != None or contacto.sexo or edaddesde != None or edadhasta != None:
            qwery = qwery + "WHERE"
        
        if contacto.id != None:
            if qa[0] == 1 and 1 not in qa[1:]:
                optionalwhere = "ID_CONTACTO = '{}' ".format(contacto.id)
                qwery = qwery + optionalwhere
            else:
                optionalwhere = "ID_CONTACTO = '{}' AND".format(contacto.id)
                qwery = qwery + optionalwhere

        if contacto.nombre != None:
            if qa[1] == 1 and 1 not in qa[2:]:
                optionalwhere = "NOMBRE_CONTACTO = '{}'".format(contacto.nombre)
                qwery = qwery + optionalwhere
            else:
                optionalwhere = "NOMBRE_CONTACTO = '{}' AND".format(contacto.nombre)
                qwery = qwery + optionalwhere
        
        if contacto.fecha_nacimiento != None:
            if qa[2] == 1 and 1 not in qa[3:]:
                optionalwhere = "FECHA_NACIMIENTO = '{}'".format(contacto.fecha_nacimiento)
                qwery = qwery + optionalwhere
            else:
                optionalwhere = "FECHA_NACIMIENTO = '{}' AND".format(contacto.fecha_nacimiento)
                qwery = qwery + optionalwhere
        
        if contacto.email != None:
            if qa[3] == 1 and 1 not in qa[4:]:
                optionalwhere = "EMAIL = '{}'".format(contacto.email)
                qwery = qwery + optionalwhere
            else:
                optionalwhere = "EMAIL = '{}' AND".format(contacto.email)
                qwery = qwery + optionalwhere
        
        if contacto.direccion != None:
            if qa[4] == 1 and 1 not in qa[5:]:
                optionalwhere = "DIRECCION = '{}'".format(contacto.direccion)
                qwery = qwery + optionalwhere
            else:
                optionalwhere = "DIRECCION = '{}' AND".format(contacto.direccion)
                qwery = qwery + optionalwhere
        
        if contacto.sexo != None:
            if qa[5] == 1 and 1 not in qa[6:]:
                optionalwhere = "SEXO = '{}'".format(contacto.sexo)
                qwery = qwery + optionalwhere
            else: 
                optionalwhere = "SEXO = '{}' AND".format(contacto.sexo)
                qwery = qwery + optionalwhere
        
        if edaddesde != None and edadhasta != None:
            if qa[6] == 1 and 1 not in qa[7:]:
                optionalwhere = "(SELECT DATEDIFF(CURDATE() ,FECHA_NACIMIENTO)) BETWEEN '{}' AND '{}'".format(edaddesde, edadhasta)
                qwery = qwery + optionalwhere
            else:
                optionalwhere = "(SELECT DATEDIFF(CURDATE() ,FECHA_NACIMIENTO)) BETWEEN '{}' AND '{}' AND".format(edaddesde, edadhasta)
                qwery = qwery + optionalwhere
            
        if atributo.ID_atributo != None:
            optionalwhere = "ID_ATRIBUTO IN '{}'".format(atributo.ID_atributo)
            qwery = qwery + optionalwhere
            
        for i in range(0, len(qa)):
            qa[i] = 0
        
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