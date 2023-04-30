from Conectores_BD import *
import hashlib

class Login_manager():
    # Encriptacion
    def MD5(str):
        return hashlib.md5(str.encode())  #MD5

    def Validar_login(usuario, passwordMD5):
        sql = "select if('"
        sql2 = "' = PASSWORD, 1, 0) as Check_pwd from USUARIOS where NOMBRE_USUARIO = '"
        sql3 = "' AND USUARIO_HABILITACION = 1"

        Query = sql + passwordMD5 + sql2 + usuario + sql3
        validacion = Conectores_BD.Query_un_valor(Query)
        
        return validacion

class LoginController():
    def login(nombre_usuario, password):
        #Encripto el input del password de usuario
        passwordMD5 = hashlib.md5(password.encode()).hexdigest()

        #consulto validez de las credenciales (password y habilitacion)
        validacion = Login_manager.Validar_login(nombre_usuario, passwordMD5)

        return validacion