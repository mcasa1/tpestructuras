from Conectores_BD import *
import hashlib

class Usuario():
    def __init__(self, ID_USUARIO,NOMBRE_USUARIO,PASSWORD,USUARIO_HABILITACION,NOMBRE_PILA_USUARIO,APELLIDO_USUARIO,DNI_USUARIO, EMAIL_USUARIO):
        self.ID_USUARIO	= ID_USUARIO
        self.NOMBRE_USUARIO	= NOMBRE_USUARIO
        self.PASSWORD = PASSWORD
        self.USUARIO_HABILITACION = USUARIO_HABILITACION
        self.NOMBRE_PILA_USUARIO = 	NOMBRE_PILA_USUARIO
        self.APELLIDO_USUARIO = APELLIDO_USUARIO
        self.DNI_USUARIO = DNI_USUARIO
        self.EMAIL_USUARIO	= EMAIL_USUARIO

class LoginController():

    Usuario_logueado = None

    def login(nombre_usuario, password):
        # Metodo que devuelve un 1 si el usuario y contraseña son correctos, 0 si no lo son

        #Encripto el input del password de usuario
        passwordMD5 = hashlib.md5(password.encode()).hexdigest()

        #consulto validez de las credenciales (password y habilitacion)
        validacion = Login_model.Validar_login(nombre_usuario, passwordMD5)

        if validacion == 1:
            usuario_log = Login_model.Datos_usuario(nombre_usuario)
            LoginController.Usuario_logueado = Usuario(usuario_log[0],usuario_log[1],usuario_log[2],usuario_log[3],usuario_log[4],usuario_log[5],usuario_log[6],usuario_log[7])

        return validacion
    def Cambiar_contraseña(password):
        # Metodo para cambiar la contraseña del usuario

        #Encripto el input del password de usuario
        passwordMD5 = hashlib.md5(password.encode()).hexdigest()
        Login_model.Update_password(passwordMD5,LoginController.Usuario_logueado)

class Login_model():
    def MD5(str):
        # Metodo para encriptar el input de password y comparar con la BD
        return hashlib.md5(str.encode())
    def Validar_login(usuario, passwordMD5):
        #Metodo que consulta a la base si el string encriptado que se puso en "contraseña" conincide con el de la base de datos
        #donde el usuario es el mismo que el ingresado en "usuario"

        sql = "select if('"
        sql2 = "' = PASSWORD, 1, 0) as Check_pwd from USUARIOS where NOMBRE_USUARIO = '"
        sql3 = "' AND USUARIO_HABILITACION = 1"

        Query = sql + passwordMD5 + sql2 + usuario + sql3
        validacion = Conectores_BD.Query_un_valor(Query)
        
        return validacion
    def Datos_usuario(Nombre_usuario):
        # Metodo que devuelve todos los datos del usuario

        sql = """SELECT `ID_USUARIO`,`NOMBRE_USUARIO`,`PASSWORD`,`USUARIO_HABILITACION`,`NOMBRE_PILA_USUARIO`,`APELLIDO_USUARIO`,`DNI_USUARIO`,`EMAIL_USUARIO`
                FROM `USUARIOS`
                WHERE NOMBRE_USUARIO = '{}'""".format(Nombre_usuario)
        Engine =  Conectores_BD.conector_mysql()
        usuario = Engine.connect().execute(text(sql))
        usuario = usuario.fetchone()        
        return usuario
    def Update_password(password,Usuario:Usuario):
        # Metodo que actualiza la contraseña en la BD

        #Conector
        MySql = Conectores_BD.conector_mysql()

        #Qwery
        qwery = """UPDATE `USUARIOS`
                    SET PASSWORD = '{}'
                    WHERE NOMBRE_USUARIO = '{}'""".format(password,Usuario.NOMBRE_USUARIO)

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()
