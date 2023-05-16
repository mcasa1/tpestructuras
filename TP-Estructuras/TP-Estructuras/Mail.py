from Conectores_BD import *
import array as array

# Clase para representar un correo electronico
class Mail:
    def __init__(self, asunto, cuerpo):
        self.asunto = asunto
        self.cuerpo = cuerpo

# Clase para controlar los correos electronicos
class MailController:
    
    mails = []  

    # Metodo para crear un correo electronico
    def crear_mail(self, asunto, cuerpo):
        mail = Mail(asunto, cuerpo)
        Mail_model.Post_mail(mail)

class Mail_model: 
    def Post_mail(mail):
        #Conector
        MySql = Conectores_BD.conector_mysql()
        
        #Creo el cursor
        cnxn = MySql.raw_connection()
            
        #Qwery
        qwery = "INSERT INTO MAIL (cuerpo, asunto) VALUES ('{}','{}')".format(mail.cuerpo, mail.asunto)

        #Ejecuto el comando y guardo cambios
        with MySql.connect() as conn:
            conn.execute(text(qwery))
            conn.commit()