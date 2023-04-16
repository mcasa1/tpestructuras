class Contacto:
    def __init__(self, nombre, email, intereses):
        self.nombre = nombre
        self.email = email
        self.intereses = intereses

class Campana:
    def __init__(self, nombre_campana, asunto, cuerpo, intereses_destinatarios):
        self.nombre_campana = nombre_campana
        self.asunto = asunto
        self.cuerpo = cuerpo
        self.intereses_destinatarios = intereses_destinatarios

class PlataformaEmailMarketing:
    def __init__(self):
        self.contactos = []
        self.campanas = []

    def agregar_contacto(self, nombre, email, intereses):
        contacto = Contacto(nombre, email, intereses)
        self.contactos.append(contacto)

    def agregar_intereses(self, email, interes):
        for contacto in self.contactos:
            if contacto.email == email:
                contacto.intereses.append(interes)
                print(f"Interes {interes} agregado a {contacto.nombre} ({contacto.email})")
                break
        else:
            print("No se encontró el contacto")

    def agregar_campana(self, nombre_campana, asunto, cuerpo, intereses_destinatarios):
        campana = Campana(nombre_campana, asunto, cuerpo, intereses_destinatarios)
        self.campanas.append(campana)

    def enviar_campana(self, nombre_campana):
        for campana in self.campanas:
            if campana.nombre_campana == nombre_campana:
                for contacto in self.contactos:
                    if set(contacto.intereses).intersection(set(campana.intereses_destinatarios)):
                        print(f"Enviando correo a {contacto.nombre} ({contacto.email}) con el asunto '{campana.asunto}' y el cuerpo '{campana.cuerpo}'...")
                break
        else:
            print("No se encontró la campaña")

# Ejemplo de uso
plataforma = PlataformaEmailMarketing()

#Agregar contactos
plataforma.agregar_contacto("Juan", "juan@gmail.com", ["moda", "deportes"])
plataforma.agregar_contacto("María", "maria@gmail.com", ["tecnología", "viajes"])
plataforma.agregar_contacto("Pedro", "pedro@gmail.com", ["moda", "hogar"])

#Agregar intereses a contacto
plataforma.agregar_intereses("juan@gmail.com", "deporte")

#Agregar campañas
plataforma.agregar_campana("Campaña 1", "Ofertas de moda", "Descuentos en ropa", ["moda"])
plataforma.agregar_campana("Campaña 2", "Ofertas de tecnología", "Descuentos en tecnología", ["tecnología"])

#Enviar campaña
plataforma.enviar_campana("Campaña 1")