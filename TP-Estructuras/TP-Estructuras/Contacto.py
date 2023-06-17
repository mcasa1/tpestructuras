import re
import time
from Conectores_BD import *
from Atributos import *
import array as array
from Brevo import *

# Clase contacto
class Contacto:
    def __init__(self, nombre=None, email=None, fecha_nacimiento=None, direccion=None, sexo=None, id_contacto=None, atributos:list=[]):
        self.id_contacto = id_contacto
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
class Contacto_Controller():

    contactos = []

    # Metodo para agregar un contacto con id unico
    def agregar_contacto(newContact: Contacto):
        brevo = Brevo_contactos()
        id_contacto = brevo.post_contacto(newContact)
        newContact.id = id_contacto.id
        Contacto_Model.Post_contacto(newContact)
    
    # Metodo para imprimir los contactos no ocultos con parametro
    def obtener_contactos_params(id_contacto, nombre, email, fecha_nacimiento, direccion, sexo):
        contacto = Contacto(id_contacto, nombre, email, fecha_nacimiento, direccion, sexo)
        datos = Contacto_Model.listar_contactos(contacto)
        for dato in datos:
            contacto_devuelto = Contacto(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])
            contactos = contactos.append(contacto_devuelto)
        return contactos

    # Metodo para imprimir los contactos con parametro
    def obtener_contactos(habilitado,id_contacto=None, nombre=None, email=None, fecha_nacimiento=None, direccion=None, sexo=None):
        datos = Contacto_Model.listar_contactos(id_contacto, nombre, email, fecha_nacimiento, direccion, sexo, habilitado)
        resultados = []
        for dato in datos:
            contacto_devuelto = Contacto(id_contacto=dato[0], nombre=dato[1], fecha_nacimiento=dato[2], email=dato[3], direccion=dato[4], sexo=dato[5])
            resultados.append(contacto_devuelto)
        return resultados

    # Metodo para ocultar un contacto
    def ocultar_contacto(email):
        Contacto_Model.ocultar_contacto(Contacto(email=email))

    #Metodo para vincular atributos a un contacto
    def agregar_atributos_contacto(contacto):
        Contacto_Model.Post_atributos_contacto(contacto)


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
    def listar_contactos_buscador(contacto, edad_desde, edad_hasta, atributo, habilitado):
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
            optionalwhere = "AND NOMBRE_CONTACTO = '{}'".format(contacto.nombre)
            qwery = qwery + optionalwhere
        
        if contacto.fecha_nacimiento != None:
                optionalwhere = "AND FECHA_NACIMIENTO = '{}'".format(contacto.fecha_nacimiento)
                qwery = qwery + optionalwhere
        
        if contacto.email != None:
                optionalwhere = "AND EMAIL = '{}'".format(contacto.email)
                qwery = qwery + optionalwhere
        
        if contacto.direccion != None:
                optionalwhere = "DIRECCION = '{}'".format(contacto.direccion)
                qwery = qwery + optionalwhere

        if contacto.sexo != None:
                optionalwhere = "AND SEXO = '{}'".format(contacto.sexo)
                qwery = qwery + optionalwhere
        
        if edad_desde != None and edad_hasta != None:
                optionalwhere = " AND (SELECT DATEDIFF(CURDATE() ,FECHA_NACIMIENTO)) BETWEEN '{}' AND '{}'".format(edad_desde, edad_hasta)
                qwery = qwery + optionalwhere
            
        if atributo.ID_atributo != None:
            optionalwhere = "AND ID_ATRIBUTO IN '{}'".format(atributo.ID_atributo)
            qwery = qwery + optionalwhere
            
        
        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
            result = conn.execute(text(qwery))
        return result
    def listar_contactos(id_contacto, nombre, email, fecha_nacimiento, direccion, sexo, habilitado):
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
                    WHERE CONTACTO_HABILITACION = {} """.format(habilitado)
                
        if id_contacto != None:
            optionalwhere = "AND ID_CONTACTO = '{}' ".format(id_contacto)
            qwery = qwery + optionalwhere
                
        if nombre != None:
            optionalwhere = "AND NOMBRE_CONTACTO = '{}'".format(nombre)
            qwery = qwery + optionalwhere
        
        if fecha_nacimiento != None:
                optionalwhere = "AND FECHA_NACIMIENTO = '{}'".format(fecha_nacimiento)
                qwery = qwery + optionalwhere
        
        if email != None:
                optionalwhere = "AND EMAIL = '{}'".format(email)
                qwery = qwery + optionalwhere
        
        if direccion != None:
                optionalwhere = "DIRECCION = '{}'".format(direccion)
                qwery = qwery + optionalwhere

        if sexo != None:
                optionalwhere = "AND SEXO = '{}'".format(sexo)
                qwery = qwery + optionalwhere           
        
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
    def Post_atributos_contacto(contacto: Contacto):
        #Conector
        MySql = Conectores_BD.conector_mysql()
        
        #Creo el cursor
        cnxn = MySql.raw_connection()
            
        #Qwery
        qwery = "INSERT INTO ATRIBUTOS_CONTACTOS (ID_ATRIBUTO, ID_CONTACTO) VALUES ('{}','{}')".format(contacto.atributos[-1].ID_atributo, contacto.id)

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()


#Contacto_Controller.agregar_contacto("Lucas", "lucas12@gmail.com", "1234/02/12", "remo 123", 0)
# Contacto_Controller.ocultar_contacto_control("tomas@gmail.com")
# Contacto_Controller.obtener_contactos_todos()
#api = Brevo()
##lucas = Contacto(id=7, email="lucas12@gmail.com",nombre = 'lucas')
##api.update_contacto(lucas)
#contacto = Contacto(id=7)
#atributo = Atributo(ID_atributo=18)
## atributo = 2
#contacto.atributos.append(atributo)
#Contacto_Controller.agregar_atributos_contacto(contacto)