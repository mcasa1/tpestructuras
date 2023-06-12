import re
import time
from Conectores_BD import *
from Atributos import *
import array as array
from Brevo import *

# Clase contacto
class Contacto:
    def __init__(self, nombre=None, email=None, fecha_nacimiento=None, direccion=None, sexo=None, id=None, atributos:list=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.sexo = sexo
        self.oculto = 1
        self.atributos = atributos
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
        contacto.id = id_contacto.id
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

    def listar_contactos(contacto, edad_desde, edad_hasta, atributo, habilitado: bool):
        atributo = Atributo()
        #Conector
        MySql = Conectores_BD.conector_mysql()
                
        #Qwery
        qwery = """ SELECT 
                        ID_CONTACTO,
                        NOMBRE_CONTACTO,    
                        FECHA_NACIMIENTO,
                        EMAIL,
                        DIRECCION,
                        SEXO 
                    FROM CONTACTOS 
                        LEFT JOIN ATRIBUTOS_CONTACTO ON 
                    WHERE CONTACTO_HABILITACION = {} """.format(habilitado)
                
        
        if contacto.id != None:
            optionalwhere = "AND ID_CONTACTO = '{}' ".format(contacto.id)
            qwery = qwery + optionalwhere
        
                
        if contacto.nombre != None:
            optionalwhere = "NOMBRE_CONTACTO = '{}'".format(contacto.nombre)
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
        
        if edad_desde != None and edad_hasta != None:
            if qa[6] == 1 and 1 not in qa[7:]:
                optionalwhere = "(SELECT DATEDIFF(CURDATE() ,FECHA_NACIMIENTO)) BETWEEN '{}' AND '{}'".format(edad_desde, edad_hasta)
                qwery = qwery + optionalwhere
            else:
                optionalwhere = "(SELECT DATEDIFF(CURDATE() ,FECHA_NACIMIENTO)) BETWEEN '{}' AND '{}' AND".format(edad_desde, edad_hasta)
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




#   TEST --- TEST --- TEST --- TEST --- TEST --- TEST --- TEST --- TEST --- TEST --- TEST --- TEST --- TEST


#Contacto_Controller.agregar_contacto("Lucas", "lucas12@gmail.com", "1234/02/12", "remo 123", 0)

# Contacto_Controller.ocultar_contacto_control("tomas@gmail.com")

# Contacto_Controller.obtener_contactos_todos()

#api = Brevo()
#lucas = Contacto(id=7, email="lucas12@gmail.com",nombre = 'lucas')
#api.update_contacto(lucas)