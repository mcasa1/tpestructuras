# Clase cliente
class Cliente:
    def __init__(self, id, nombre, email, fecha_nacimiento, direccion, sexo):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.sexo = sexo
        self.oculto = False

# Clase para manejar los clientes
class ClienteController:
    def __init__(self):
        self.clientes = []

    # Método para agregar un cliente con id único
    def agregar_cliente(self, nombre, email, fecha_nacimiento, direccion, sexo):
        id = len(self.clientes) + 1
        cliente = Cliente(id, nombre, email, fecha_nacimiento, direccion, sexo)
        self.clientes.append(cliente)
    
    # Método para imprimir los clientes no ocultos
    def obtener_clientes(self):
        clientes = []
        for cliente in self.clientes:
            if not cliente.oculto:
                clientes.append(cliente)
        return clientes

    # Método para ocultar un cliente
    def ocultar_cliente(self, email):
        for cliente in self.clientes:
            if cliente.email == email:
                cliente.oculto = True
                print(f"Cliente {cliente.nombre} ocultado")
                break
        else:
            print("No se encontró el cliente")

# Clase de atributos
class Atributo:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

# Clase para manejar los atributos
class AtributoController:
    def __init__(self):
        self.atributos = []

    # Método para agregar un atributo
    def agregar_atributo(self, nombre, descripcion):
        atributo = Atributo(nombre, descripcion)
        self.atributos.append(atributo)

    # obtener atributos
    def obtener_atributos(self):
        atributos = []
        for atributo in self.atributos:
            atributos.append(atributo)
        return atributos
 
    # Método para eliminar un atributo
    def eliminar_atributo(self, nombre):
        for atributo in self.atributos:
            if atributo.nombre == nombre:
                self.atributos.remove(atributo)
                print(f"Atributo {atributo.nombre} eliminado")
                break
        else:
            print("No se encontró el atributo")

# Clase cliente x atributos
class ClienteAtributo:
    def __init__(self, cliente, atributos):
        self.cliente = cliente
        self.atributos = atributos
        
# Clase para manejar los clientes por atributos
class AtributoClienteController:
    def __init__(self, clientes_controller, atributos_controller):
        self.atributos_clientes = []  # lista de atributos asignados a clientes
        self.atributos_controller = atributos_controller
        self.clientes_controller = clientes_controller

    def agregar_atributo_cliente(self, email_cliente, nombre_atributo):
        for cliente in self.clientes_controller.clientes:
            if cliente.email == email_cliente:
                for atributo in self.atributos_controller.atributos:
                    for i in range(len(nombre_atributo)):
                        if atributo.nombre == nombre_atributo[i]:
                            # crear una instancia de ClienteAtributo con el cliente y el atributo correspondiente
                            self.atributos_clientes.append(ClienteAtributo(cliente, atributo))
                            print(f"Atributo {atributo.nombre} agregado al cliente {cliente.nombre}")
                            break
                    else:
                        continue
                    break
        else:
            print("No se encontró el cliente")

# Clase para mantener una lista de clientes
class ListaClientes:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.clientes = []  # lista de clientes en la lista

# Clase para controlar la lista de clientes
class ListaClientesController:
    def __init__(self, clientes_atributo_controller):
        self.listas = []  # lista de ListasClientes
        self.clientes_atributo_controller = clientes_atributo_controller

    # Método para crear una lista de clientes que no estén ocultos y tengan ciertos atributos
    def crear_lista(self, nombre, descripcion, atributos):
        lista = ListaClientes(nombre, descripcion)
        for cliente in self.clientes_atributo_controller.clientes_controller.clientes:
            if not cliente.oculto and set(atributos).issubset(set(atributo.atributos.nombre for atributo in self.clientes_atributo_controller.atributos_clientes if atributo.cliente == cliente)):
                lista.clientes.append(cliente)
                print(f"Cliente {cliente.nombre} agregado a la lista {lista.nombre}")
        self.listas.append(lista)

# Clase para representar un correo electrónico
class Mail:
    def __init__(self, asunto, cuerpo):
        self.asunto = asunto
        self.cuerpo = cuerpo

# Clase para controlar los correos electrónicos
class MailController:
    def __init__(self):
        self.mails = []  # lista de correos electrónicos creados

    # Método para crear un correo electrónico
    def crear_mail(self, asunto, cuerpo):
        mail = Mail(asunto, cuerpo)
        self.mails.append(mail)

    # Método para listar los correos electrónicos creados
    def listar_mails(self):
        for mail in self.mails:
            print(f"{mail.asunto} - {mail.cuerpo}")

# Clase Campana
class Campana:
    def __init__(self, nombre_campana, descripcion):
        self.nombre_campana = nombre_campana
        self.descripcion = descripcion
        self.lista_clientes = []
        self.mail = None

class CampanaController:
    def __init__(self, lista_clientes_controller, lista_clientes):
        self.campañas = [] 
        self.lista_clientes_controller = lista_clientes_controller
        self.lista_clientes = lista_clientes

    # Método para crear una campaña
    def crear_campana(self, nombre_campana, descripcion):
        campana = Campana(nombre_campana, descripcion)
        self.campañas.append(campana)

    # Método para agregar una lista de clientes a una campaña
    def asignar_lista_clientes(self, nombre_campana, nombre_lista):
        campana_encontrada = False
        lista_encontrada = False
        
        for campana in self.campañas:
            if campana.nombre_campana == nombre_campana:
                campana_encontrada = True
                for lista in self.lista_clientes_controller.listas:
                    if lista.nombre == nombre_lista:
                        lista_encontrada = True
                        campana.lista_clientes = lista.clientes
                        print(f"Lista de clientes '{nombre_lista}' asignada a la campaña '{nombre_campana}'")
                        break

        if not campana_encontrada:
            print(f"No se encontró la campaña '{nombre_campana}'")

        if not lista_encontrada:
            print(f"No se encontró la lista de clientes '{nombre_lista}'")

    # Método para agregar un mail a una campaña
    def asignar_mail(self, nombre_campana, asunto,):
        for campana in self.campañas:
            if campana.nombre_campana == nombre_campana:
                for mail in self.lista_clientes.mails:
                    if mail.asunto == asunto:
                        campana.mail = mail
                        print(f"Mail '{asunto}' asignado a la campaña '{nombre_campana}'")
                        break
                else:
                    print(f"No se encontró el mail '{asunto}'")
                break
        else:
            print(f"No se encontró la campaña '{nombre_campana}'")

    # Método para enviar una campaña
    def enviar_campana(self, nombre_campana):
        # Buscar la campaña correspondiente
        for campana in self.campañas:
            if campana.nombre_campana == nombre_campana:
                if campana.mail is None:
                    print("No se ha agregado un mail a la campaña")
                else:
                    for cliente in campana.lista_clientes:
                        print(f"Se envía mail a {cliente.nombre} con asunto {campana.mail.asunto} y cuerpo {campana.mail.cuerpo}")
                break
        else:
            print("No se encontró la campaña")


# Creamos una instancia del controlador de clientes
cliente_controller = ClienteController()

# Creamos una instancia del controlador de atributos
atributo_controller = AtributoController()

# Creamos una instancia del controlador de atributos de clientes
cliente_atributo_controller = AtributoClienteController(cliente_controller, atributo_controller)

# Creamos una instancia del controlador de listas de clientes
lista_clientes_controller = ListaClientesController(cliente_atributo_controller)

# Creamos una instancia del controlador de correos
mail_controller = MailController()

# Creamos una instancia del controlador de campañas
campana_controller = CampanaController(lista_clientes_controller, mail_controller)

#Menú principal
def menu_principal():
    print(" ")
    print("Menú principal")
    print("1. Clientes")
    print("2. Atributos")
    print("3. Asignar atributo a cliente")
    print("4. Crear lista de clientes")
    print("5. Campañas")
    print("6. Mails")
    print("7. Salir")

#Menú de clientes
def menu_clientes():
    print(" ")
    print("Menú de clientes")
    print("1. Agregar cliente")
    print("2. Listar clientes")
    print("3. Ocultar cliente")
    print("4. Volver")

#Menú de atributos
def menu_atributos():
    print(" ")
    print("Menú de atributos")
    print("1. Agregar atributo")
    print("2. Listar atributos")
    print("3. Volver")

#Menú de campañas
def menu_campañas():
    print(" ")
    print("Menú de campañas")
    print("1. Crear campaña")
    print("2. Asignar lista de clientes a campaña")
    print("3. Asignar mail a campaña")
    print("4. Enviar campaña")
    print("5. Volver")

#Menú de mails
def menu_mails():
    print(" ")
    print("Menú de mails")
    print("1. Agregar mail")
    print("2. Listar mails")
    print("3. Volver")

#while
while True:
    menu_principal()
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        while True:
            menu_clientes()
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                nombre = input("Ingrese el nombre del cliente: ")
                email = input("Ingrese el email del cliente: ")
                fecha_nacimiento = input("Ingrese la fecha de nacimiento del cliente: ")
                direccion = input("Ingrese la dirección del cliente: ")
                sexo = input("Ingrese el sexo del cliente: ")
                cliente_controller.agregar_cliente(nombre, email, fecha_nacimiento, direccion, sexo)
            elif opcion == "2":
                cliente_controller.obtener_clientes()
            elif opcion == "3":
                cliente_controller.ocultar_cliente()
            elif opcion == "4":
                break
            else:
                print("Opción inválida")
    elif opcion == "2":
        while True:
            menu_atributos()
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                nombre = input("Ingrese el nombre del atributo: ")
                descripcion = input("Ingrese la descripción del atributo: ")
                atributo_controller.agregar_atributo(nombre, descripcion)
            elif opcion == "2":
                atributo_controller.obtener_atributos()
            elif opcion == "3":
                break
            else:
                print("Opción inválida")
    elif opcion == "3":
        while True:
                mail_cliente = input("Ingrese el mail del cliente: ")
                nombre_atributo = input("Ingrese el nombre del atributo: ")
                cliente_atributo_controller.agregar_atributo_cliente(mail_cliente, nombre_atributo)
                break
    elif opcion == "4":
        while True:
                nombre_lista = input("Ingrese el nombre de la lista: ")
                descripcion_lista = input("Ingrese la descripción de la lista: ")
                atributos_lista = input("Ingrese los atributos de la lista: ")
                lista_clientes_controller.crear_lista(nombre_lista, descripcion_lista, atributos_lista)
                break
    elif opcion == "5":
        while True:
            menu_campañas()
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                nombre_campaña = input("Ingrese el nombre de la campaña: ")
                descripcion_campaña = input("Ingrese la descripción de la campaña: ")
                campana_controller.crear_campana(nombre_campaña, descripcion_campaña)
            elif opcion == "2":
                nombre_campaña = input("Ingrese el nombre de la campaña: ")
                nombre_lista = input("Ingrese el nombre de la lista: ")
                campana_controller.asignar_lista_clientes(nombre_campaña, nombre_lista)
            elif opcion == "3":
                nombre_campaña = input("Ingrese el nombre de la campaña: ")
                nombre_mail = input("Ingrese el nombre del mail: ")
                campana_controller.asignar_mail(nombre_campaña, nombre_mail)
            elif opcion == "4":

                nombre_campaña = input("Ingrese el nombre de la campaña: ")
                campana_controller.enviar_campana(nombre_campaña)
            elif opcion == "5":
                break
            else:
                print("Opción inválida")
    elif opcion == "6":
        while True:
            menu_mails()
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                asunto = input("Ingrese el asunto del mail: ")
                cuerpo = input("Ingrese el cuerpo del mail: ")
                mail_controller.crear_mail(asunto, cuerpo)
            elif opcion == "2":
                mail_controller.listar_mails()
            elif opcion == "3":
                break
            else:
                print("Opción inválida")
    elif opcion == "7":
        break
    else:
        print("Opción inválida")


# # Agregamos algunos clientes
# cliente_controller.agregar_cliente("Juan", "juan@gmail.com", "23/10/1990", "av. siempre viva 123","M")
# cliente_controller.agregar_cliente("Pedro", "pedro@gmail.com", "4/10/1990", "av. siempre viva 125","M")



# # Agregamos algunos atributos
# atributo_controller.agregar_atributo("A", "Atributo A")
# atributo_controller.agregar_atributo("B", "Atributo B")


# # Asignamos atributos a los clientes
# cliente_atributo_controller.agregar_atributo_cliente("juan@gmail.com", ["A", "B"])
# cliente_atributo_controller.agregar_atributo_cliente("pedro@gmail.com", ["A"])


# # Creamos una lista de clientes
# lista_clientes_controller.crear_lista("Lista A", "Lista de clientes con atributo A", ["A"])
# lista_clientes_controller.crear_lista("Lista B", "Lista de clientes con atributo B", ["B"])



# # Creamos algunos correos
# mail_controller.crear_mail("Oferta para A", "Oferta de A")
# mail_controller.crear_mail("Oferta para B", "Oferta de B")



# #Crear campaña
# campana_controller.crear_campana("Campana A", "Campana para clientes con atributo A")
# campana_controller.crear_campana("Campana B", "Campana para clientes con atributo B")

# #Agregar lista de clientes a campaña
# campana_controller.asignar_lista_clientes("Campana A", "Lista A")
# campana_controller.asignar_lista_clientes("Campana B", "Lista B")

# #Agregar mail a campaña
# campana_controller.asignar_mail("Campana A", "Oferta para A")
# campana_controller.asignar_mail("Campana B", "Oferta para B")

# #Enviar campaña
# campana_controller.enviar_campana("Campana A")
# campana_controller.enviar_campana("Campana B")