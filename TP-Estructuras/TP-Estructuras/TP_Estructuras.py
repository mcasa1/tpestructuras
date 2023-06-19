import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkcalendar import Calendar
from tktimepicker import AnalogPicker, AnalogThemes,SpinTimePickerModern,constants
from turtle import bgcolor

from Login import LoginController
from Atributos import AtributosController
from Contacto import Contacto_Controller, Contacto
from campana import CampañaController, Campaña
from datetime import *

class tkinterStyles():
    def estiloTabla():
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('cooper', 11)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('cooper', 13,'bold')) # Modify the font of the headings
        #style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        return style

#VISTAS
class Login(tk.Frame):
    def __init__(self, container, controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "white")
        self.entrada_usuario = tk.StringVar()

        # LABEL TITULO
        titulo = tk.Label(self, pady = 5, bg = 'white', text = 'Log-in',font = 'cooper 30 bold', fg = 'deep pink')
        titulo.pack(
            fill='x',
            side='top')
        # LABEL USUSARIO
        usuario = tk.Label(self, pady = 5, bg = 'white', text = 'Usuario',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        usuario.pack(
            fill='x',
            side='top')
        # txt USUSARIO
        txt_usuario = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_usuario.pack(
            fill='x',
            side='top')
        # LABEL pswd
        pswd = tk.Label(self, pady = 5, bg = 'white', text = 'Contraseña',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        pswd.pack(
            fill='x',
            side='top')
        # txt pswd
        txt_pswd = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink', show="*")
        txt_pswd.pack(
            fill='x',
            side='top')

        tk.Button(self,
                text='Iniciar sesion',
                bg = 'white',
                fg = 'deep pink',
                font = 'cooper 15',
                cursor='hand2',
                command=lambda: Login.LOG(self,txt_usuario.get(), txt_pswd.get(),controller)).pack(side='bottom') #,expand=True,fill='x')
    def open_ContraseñaIncorrecta(self):
           window = ContraseñaIncorrecta(self)
           window.grab_set()
    def LOG(self,usuario, contraseña, controller):
        try:
            validacion = LoginController.login(usuario, contraseña)
            
            if validacion == 1:
                APP.show_frame( controller, HomeView )
            elif validacion == 0:
                Login.open_ContraseñaIncorrecta(self)
        except:
            Login.open_ContraseñaIncorrecta(self)
            
    #Menu HOME
class HomeView(tk.Frame):
    def __init__(self, container, controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "white")
        self.entrada_usuario = tk.StringVar()

        # LABEL TITULO
        titulo = tk.Label(self, pady = 5, bg = 'white', text = 'GESTOR DE CAMPAÑAS DE MARKETING',font = 'cooper 30 bold', fg = 'deep pink')
        titulo.pack(
            fill='x',
            side='top')

        tk.Button(self,
                text='Campañas ',
                bg = 'white',
                fg = 'deep pink',
                font = 'cooper 15',
                cursor='hand2',
                command=lambda: controller.show_frame( CampañasMenu )).pack(side='left',expand=True,fill='both')
        tk.Button(self,
                text='Contactos',
                bg = 'white',
                fg = 'deep pink',
                font = 'cooper 15',
                cursor='hand2',
                command=lambda: controller.show_frame( ContactosMenu )).pack(side='left',expand=True,fill='both')
        #tk.Button(self,
        #        text='  Mails  ',
        #        bg = 'white',
        #        fg = 'deep pink',
        #        font = 'cooper 15',
        #        cursor='hand2',
        #        command=lambda: controller.show_frame( MailMenu )).pack(side='left',expand=True,fill='both')
  
#Sub menues
class ContactosMenu(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "white")

        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Menu Contactos',font = 'cooper 25', fg = 'deep pink')
        titulo.pack(fill='both',side='top')

        tk.Button(self,
                    text='Contactos',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( View_GestionarContactos )).pack(side='left', fill='both',expand=True)       
        tk.Button(self,
                    text='Atributos',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( View_GestionarAtributosClientes )).pack(side='left', fill='both',expand=True)
        tk.Button(self,
                    text='Volver',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda:controller.show_frame( HomeView )).pack(side='bottom', fill='x')
#class MailMenu(tk.Frame):
#    def __init__(self, container,controller,*args, **kwargs):
#        super().__init__(container, *args, **kwargs)
#        self.configure(bg = "white")

#        #LABEL TITULO
#        titulo = tk.Label(self, bg = 'white', text = 'GESTOR DE CLIENTES',font = 'cooper 25', fg = 'deep pink')
#        titulo.pack(fill='both',side='top')

#        tk.Button(self,
#                    text='aaaaa',
#                    bg = 'white',
#                    fg = 'deep pink',
#                    font = 'cooper 15',
#                    cursor='hand2',
#                    command=lambda:controller.show_frame( SubMenu2MainView )).pack(side='left', fill='both',expand=True)       
#        tk.Button(self,
#                    text='aaaaa',
#                    bg = 'white',
#                    fg = 'deep pink',
#                    font = 'cooper 15',
#                    cursor='hand2',
#                    command=lambda:controller.show_frame( SubMenu2MainView )).pack(side='left', fill='both',expand=True)
#        tk.Button(self,
#                    text='Volver',
#                    bg = 'white',
#                    fg = 'deep pink',
#                    font = 'cooper 10',
#                    cursor='hand2',
#                    command=lambda:controller.show_frame( HomeView )).pack(side='bottom', fill='x')
class CampañasMenu(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "white")

        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'GESTOR DE CLIENTES',font = 'cooper 25', fg = 'deep pink')
        titulo.pack(fill='both',side='top')

        tk.Button(self,
                    text='Campañas',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( View_Campañas )).pack(side='left', fill='both',expand=True)       
        tk.Button(self,
                    text='Listas de clientes',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( View_ListasContactos )).pack(side='left', fill='both',expand=True)
        tk.Button(self,
                    text='Volver',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda:controller.show_frame( HomeView )).pack(side='bottom', fill='x')

#MENUES 3ERA CAPA
# --- 0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 --- 

# CONTACTOS
# VISTAS Y POP-UPs DE CONTACTOS
class View_GestionarContactos(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "white")

        #BOTON VOLVER
        tk.Button(self,
                    text='Volver',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda:controller.show_frame( ContactosMenu )).pack(side='bottom', fill='x')

        tk.Button(self,
                    text='Eliminar',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_GestionarContactos.Eliminar_Contacto(self)).pack(side='bottom', fill='x')

        #BOTON AGREGAR ATRIBUTO
        tk.Button(self,
                    text='Agregar',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_GestionarContactos.Agregar_Contacto(self)).pack(side='bottom', fill='x')


        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Contactos',font = 'cooper 25', fg = 'deep pink')
        titulo.pack(fill='both',side='top')
        espacio = tk.Label(self, bg = 'white', text = '  ',font = 'cooper 25', fg = 'deep pink')
        espacio.pack(fill='both',side='top')

        #CONFIGURACION DE LA TABLA
        tkinterStyles.estiloTabla()

        tree = ttk.Treeview(self, show='headings', columns=['ID_CONTACTO','NOMBRE_CONTACTO','FECHA_NACIMIENTO','EMAIL','DIRECCION','SEXO'], style= "mystyle.Treeview")
        tree.heading('ID_CONTACTO', text='ID CONTACTO')
        tree.heading('NOMBRE_CONTACTO', text='NOMBRE')
        tree.heading('FECHA_NACIMIENTO', text='NACIMIENTO')
        tree.heading('EMAIL', text='EMAIL')
        tree.heading('DIRECCION', text='DIRECCION')
        tree.heading('SEXO', text='SEXO')

        View_GestionarContactos.obtener_contactos(tree)

        #BOTON ACTUALIZAR
        tk.Button(self,
                    text='Actualizar',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_GestionarContactos.obtener_contactos(tree)).pack(side='bottom', fill='x')
    def obtener_contactos(tree):
        pass
        for i in tree.get_children():
            tree.delete(i)
        list_contactos = Contacto_Controller.obtener_contactos(habilitado=1)

        for contacto in list_contactos:
            tree.insert('',tk.END ,values=[contacto.id_contacto,contacto.nombre,contacto.fecha_nacimiento,contacto.email,contacto.direccion,contacto.sexo])
            tree.pack(side='top', fill='both')
    def Agregar_Contacto(self):
        window = AgregarContacto(self)
        window.grab_set()
    def Eliminar_Contacto(self):
        window = EliminarContacto(self)
        window.grab_set() 

#Pop-ups para llenado de formularios
class AgregarContacto(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x620')
        self.title('Agregar contacto')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Agregar un contacto',font = 'cooper 16', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        # LABEL NOMBRE
        titulo_nombre = tk.Label(self, pady = 5, bg = 'white', text = 'Nombre y apellido',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_nombre.pack(
            fill='x',
            side='top')
        # ENTRY NOMBRE
        txt_nombre = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_nombre.pack(
            fill='x',
            side='top')


        # LABEL MAIL
        titulo_mail = tk.Label(self, pady = 5, bg = 'white', text = 'E-mail',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_mail.pack(
            fill='x',
            side='top')
        # ENTRY MAIL
        txt_mail= tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_mail.pack(
            fill='x',
            side='top')

        # LABEL FEC_NAC
        titulo_mail = tk.Label(self, pady = 5, bg = 'white', text = 'Fecha de nacimiento',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_mail.pack(
            fill='x',
            side='top')
        # ENTRY CALENDARIO
        #guardar en una variable el dia, mes y año de hoy
        dia = date.today().day
        mes = date.today().month
        año = date.today().year
        calendario = Calendar(self,locale='es_ES' ,date_pattern='y-mm-dd', selectmode = 'day',year = año, month = mes, day = dia)
        calendario.pack(fill='x',side='top')

        # LABEL DIRECCION
        titulo_direccion= tk.Label(self, pady = 5, bg = 'white', text = 'Dirección',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_direccion.pack(
            fill='x',
            side='top')
        # ENTRY DIRECCION
        txt_direccion= tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_direccion.pack(
            fill='x',
            side='top')

        # LABEL SEXO
        titulo_sexo= tk.Label(self, pady = 5, bg = 'white', text = 'Sexo',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_sexo.pack(
            fill='x',
            side='top')
        # ENTRY SEXO
        sexo_box = ttk.Combobox(self,
            state="readonly",
            values=["Masculino", "Femenino"])

        sexo_box.current(0)
        sexo_box.pack(side='top', fill='both',expand=True)


        tk.Button(self,
                    text='Cargar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=lambda: AgregarContacto.post_contacto(self,
                                                                  txt_nombre.get(),
                                                                 txt_mail.get(),
                                                                calendario.get_date(),
                                                               txt_direccion.get(),
                                                              sexo_box.get()
                                                              )
                   ).pack(side='top', fill='both',expand=True)

        tk.Button(self,
                    text='Cerrar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='top', fill='both',expand=True)
    def post_contacto(self,nombre,mail, fec_nac, direccion, sexo):
        try:
            if sexo == 'Masculino':
                sexo = 0
            else:
                sexo = 1
            nuevo_contacto = Contacto(nombre, mail, fec_nac, direccion, sexo)
            Contacto_Controller.agregar_contacto(nuevo_contacto)
            AgregarContacto.open_CargaExitosa(self)
        except:
            AgregarContacto.open_CargaError(self)
    def open_CargaExitosa(self):
           window = CargaExitosa(self)
           window.grab_set()
    def open_CargaError(self):
           window = CargaError(self)
           window.grab_set()    
class EliminarContacto(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x180')
        self.title('Eliminar contacto')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Eliminar un contacto',font = 'cooper 16', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        # LABEL USUSARIO
        titulo_mail = tk.Label(self, pady = 5, bg = 'white', text = 'E-mail',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_mail.pack(
            fill='x',
            side='top')
        # txt USUSARIO
        txt_mail = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_mail.pack(
            fill='x',
            side='top')

        tk.Button(self,
                    text='Eliminar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=lambda: EliminarContacto.hide_contact(self,txt_mail.get())).pack(side='top', fill='both',expand=True)

        tk.Button(self,
                    text='Cerrar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='top', fill='both',expand=True)
    def hide_contact(self,mail):
        try:
            Contacto_Controller.ocultar_contacto(mail)
            EliminarContacto.open_EliminadoExitoso(self)
        except:
            EliminarContacto.open_EliminadoError(self)

    def open_EliminadoExitoso(self):
           window = EliminadoExitoso(self)
           window.grab_set()
    def open_EliminadoError(self):
           window = EliminadoError(self)
           window.grab_set()  

# --- 0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 --- 

# ATRIBUTOS
# VISTAS Y POP-UPs DE ATRIBUTOS DE CONTACTOS
class View_GestionarAtributosClientes(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "white")

        #BOTON VOLVER
        tk.Button(self,
                    text='Volver',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda:controller.show_frame( ContactosMenu )).pack(side='bottom', fill='x')

        tk.Button(self,
                    text='Eliminar',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_GestionarAtributosClientes.Eliminar_Atributo(self)).pack(side='bottom', fill='x')

        #BOTON AGREGAR ATRIBUTO
        tk.Button(self,
                    text='Agregar',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_GestionarAtributosClientes.Agregar_Atributo(self)).pack(side='bottom', fill='x')


        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Atributos de clientes',font = 'cooper 25', fg = 'deep pink')
        titulo.pack(fill='both',side='top')
        espacio = tk.Label(self, bg = 'white', text = '  ',font = 'cooper 25', fg = 'deep pink')
        espacio.pack(fill='both',side='top')

        #CONFIGURACION DE LA TABLA
        tkinterStyles.estiloTabla()

        tree = ttk.Treeview(self, show='headings', columns=['ID_ATRIBUTO','ATRIBUTO_DESCRIPCION'], style= "mystyle.Treeview")
        tree.heading('ID_ATRIBUTO', text='ID DE ATRIBUTO')
        tree.heading('ATRIBUTO_DESCRIPCION', text='DESCRIPCION')

        View_GestionarAtributosClientes.obtener_atributos(tree)

        #BOTON ACTUALIZAR
        tk.Button(self,
                    text='Actualizar',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_GestionarAtributosClientes.obtener_atributos(tree)).pack(side='bottom', fill='x')
    def obtener_atributos(tree):
        for i in tree.get_children():
            tree.delete(i)
        lista_atributos = AtributosController.obtener_atributos()

        for row in lista_atributos:
            tree.insert('',tk.END ,values=[row.ID_atributo,row.AtributoDescripcion])
            tree.pack(side='top', fill='both')
    def Agregar_Atributo(self):
        window = AgregarAtributo(self)
        window.grab_set()
    def Eliminar_Atributo(self):
        window = EliminarAtributo(self)
        window.grab_set()         

#Pop-ups para llenado de formularios
class AgregarAtributo(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x180')
        self.title('Agregar atributo')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Agregar un atributo de contacto',font = 'cooper 16', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        # LABEL USUSARIO
        titulo_atributo = tk.Label(self, pady = 5, bg = 'white', text = 'Nombre del atributo',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_atributo.pack(
            fill='x',
            side='top')
        # txt USUSARIO
        txt_atributo = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_atributo.pack(
            fill='x',
            side='top')

        tk.Button(self,
                    text='Cargar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=lambda: AgregarAtributo.post_atributo(self,txt_atributo.get())).pack(side='top', fill='both',expand=True)

        tk.Button(self,
                    text='Cerrar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='top', fill='both',expand=True)
    def post_atributo(self,nombre_atributo):
        try:
            AtributosController.agregar_atributo(nombre_atributo)
            AgregarAtributo.open_CargaExitosa(self)
        except:
            AgregarAtributo.open_CargaError(self)
    def open_CargaExitosa(self):
           window = CargaExitosa(self)
           window.grab_set()
    def open_CargaError(self):
           window = CargaError(self)
           window.grab_set()    
class EliminarAtributo(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x180')
        self.title('Eliminar atributo')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Eliminar un atributo de contacto',font = 'cooper 16', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        # LABEL USUSARIO
        titulo_atributo = tk.Label(self, pady = 5, bg = 'white', text = 'Nombre del atributo',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_atributo.pack(
            fill='x',
            side='top')
        # txt USUSARIO
        txt_atributo = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_atributo.pack(
            fill='x',
            side='top')

        tk.Button(self,
                    text='Eliminar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=lambda: EliminarAtributo.delete_atributo(self,txt_atributo.get())).pack(side='top', fill='both',expand=True)

        tk.Button(self,
                    text='Cerrar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='top', fill='both',expand=True)
    def delete_atributo(self,nombre_atributo):
        try:
            AtributosController.eliminar_atributo(nombre_atributo)
            EliminarAtributo.open_EliminadoExitoso(self)
        except:
            EliminarAtributo.open_EliminadoError(self)

    def open_EliminadoExitoso(self):
           window = EliminadoExitoso(self)
           window.grab_set()
    def open_EliminadoError(self):
           window = EliminadoError(self)
           window.grab_set()  

# --- 0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 --- 


# LISTAS DE CONTACTOS
class View_ListasContactos(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "white")

        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Submenu1',font = 'cooper 25', fg = 'deep pink')
        titulo.pack(fill='both',side='top')

        tk.Button(self,
                    text='aaaaa',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( SubMenu1MainView )).pack(side='left', fill='both',expand=True)       
        tk.Button(self,
                    text='aaaaa',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( SubMenu1MainView )).pack(side='left', fill='both',expand=True)
        tk.Button(self,
                    text='Volver',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda:controller.show_frame( HomeView )).pack(side='bottom', fill='x')



# --- 0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 --- 

# CAMPAÑAS
# VISTAS Y POP-UPs DE CAMPAÑAS
class View_Campañas(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "white")

        #BOTON VOLVER
        tk.Button(self,
                    text='Volver',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda:controller.show_frame( ContactosMenu )).pack(side='bottom', fill='x')

        tk.Button(self,
                    text='Eliminar',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_Campañas.Eliminar_Campaña(self)).pack(side='bottom', fill='x')

        #BOTON AGREGAR ATRIBUTO
        tk.Button(self,
                    text='Agregar',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_Campañas.Crear_Campaña(self)).pack(side='bottom', fill='x')


        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Campañas',font = 'cooper 25', fg = 'deep pink')
        titulo.pack(fill='both',side='top')
        espacio = tk.Label(self, bg = 'white', text = '  ',font = 'cooper 25', fg = 'deep pink')
        espacio.pack(fill='both',side='top')

        #CONFIGURACION DE LA TABLA
        tkinterStyles.estiloTabla()

        tree = ttk.Treeview(self, show='headings', columns=['ID_CAMPAÑA', 'NOMBRE_CAMPAÑA', 'DESCRIPCION_CAMPAÑA','FECHA_ENVIO','NOMBRE_LISTA_CONTACTOS','ID_MAIL'], style= "mystyle.Treeview")
        tree.heading('ID_CAMPAÑA', text='ID')
        tree.heading('NOMBRE_CAMPAÑA', text='Nombre')
        tree.heading('DESCRIPCION_CAMPAÑA', text='Asunto')
        tree.heading('FECHA_ENVIO', text='Fecha de envio')
        tree.heading('NOMBRE_LISTA_CONTACTOS', text='Lista contactos')
        tree.heading('ID_MAIL', text='Template')

        View_Campañas.Obtener_Campañas(tree)

        #BOTON ACTUALIZAR
        tk.Button(self,
                    text='Actualizar',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_Campañas.Obtener_Campañas(tree)).pack(side='bottom', fill='x')
    def Obtener_Campañas(tree):
        for i in tree.get_children():
            tree.delete(i)
        lista_campañas = CampañaController.obtener_campañas()

        for campaña in lista_campañas:
            tree.insert('',tk.END ,values=[campaña.id_campaña,campaña.nombre_campaña,campaña.descripcion_campaña,campaña.fecha_envio,campaña.ID_lista_contactos,campaña.id_mail])
            tree.pack(side='top', fill='both')
    def Crear_Campaña(self):
        window = CrearCampaña(self)
        window.grab_set()
    def Eliminar_Campaña(self):
        window = EliminarCampaña(self)
        window.grab_set()         

#Pop-ups para llenado de formularios
class CrearCampaña(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x600')
        self.title('Nueva campaña')

        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Crear una nueva campaña',font = 'cooper 16', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        # --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 ---
        # LABEL NOMBRE_CAMPAÑA
        titulo_nombre = tk.Label(self, pady = 5, bg = 'white', text = 'Nombre de la campaña',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_nombre.pack(
            fill='x',
            side='top')
        # txt USUSARIO
        txt_nombre = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_nombre.pack(
            fill='x',
            side='top')

        # --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 ---
        # LABEL DESCRIPCION CAMPAÑA
        titulo_descripcion = tk.Label(self, pady = 5, bg = 'white', text = 'Descripción de la campaña',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_descripcion.pack(
            fill='x',
            side='top')
        # txt DESCRIPCION CAMPAÑA
        txt_descripcion = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_descripcion.pack(
            fill='x',
            side='top')

        # --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 ---
        # LABEL FECHA ENVIO
        titulo_Fecha = tk.Label(self, pady = 5, bg = 'white', text = 'Fecha y hora de envio',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_Fecha.pack(
            fill='x',
            side='top')
        # ENTRY CALENDARIO
        #guardar en una variable el dia, mes y año de hoy
        dia = date.today().day
        mes = date.today().month
        año = date.today().year
        calendario = Calendar(self,locale='es_ES' ,date_pattern='y-mm-dd', selectmode = 'day',year = año, month = mes, day = dia)
        calendario.pack(fill='x',side='top')

        # ENTRY RELOJ
        time_picker = SpinTimePickerModern(self)
        time_picker.addAll(constants.HOURS24)  # adds hours clock, minutes and period
        time_picker.configureAll(bg="#404040", height=1, fg="#ffffff", font=("Times", 16), hoverbg="#404040",
                                hovercolor="#F12BF5", clickedbg="#2e2d2d", clickedcolor="#F12BF5")
        time_picker.configure_separator(bg="#404040", fg="#ffffff")
        time_picker.pack(fill='x',side='top')

        # --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 ---
        # LABEL LISTA CONTACTOS
        titulo_descripcion = tk.Label(self, pady = 5, bg = 'white', text = 'Código de la lista de contactos',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_descripcion.pack(
            fill='x',
            side='top')
        # txt LISTA CONTACTOS
        txt_lista_contactos = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_lista_contactos.pack(
            fill='x',
            side='top')

        # --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 ---
        # LABEL MAIL
        titulo_mail = tk.Label(self, pady = 5, bg = 'white', text = 'Código del template',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_mail.pack(
            fill='x',
            side='top')
        # txt MAIL
        txt_mail = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_mail.pack(
            fill='x',
            side='top')

        # --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 --- 0 ---

        tk.Button(self,
                    text='Cargar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=lambda: CrearCampaña.post_campaña(self,Campaña(fecha_envio= CrearCampaña.getDatetime(calendario.get_date(), time_picker.time()) ,nombre_campaña=txt_nombre.get(),descripcion_campaña= txt_descripcion.get(),ID_lista_contactos=int(txt_lista_contactos.get()), id_mail=int(txt_mail.get())))).pack(side='top', fill='both',expand=True)

        tk.Button(self,
                    text='Cerrar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='top', fill='both',expand=True)
    
    def getDatetime(datePart, timePart):
        #transformar un string en date
        datePart = datetime.strptime(datePart, '%Y-%m-%d').date()

        tiempo = time(timePart[0], timePart[1])


        #crear un datetime a partir de un objeto date y una tupla con los valores de horas y minutos
        return datetime.combine(datePart, tiempo)
    def post_campaña(self,Campaña: Campaña):
        #try:
            CampañaController.crear_campaña(Campaña)
            CrearCampaña.open_CargaExitosa(self)
        #except:
        #    AgregarAtributo.open_CargaError(self)
    def open_CargaExitosa(self):
           window = CargaExitosa(self)
           window.grab_set()
    def open_CargaError(self):
           window = CargaError(self)
           window.grab_set()    
class EliminarCampaña(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x180')
        self.title('Eliminar atributo')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Eliminar un atributo de contacto',font = 'cooper 16', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        # LABEL USUSARIO
        titulo_atributo = tk.Label(self, pady = 5, bg = 'white', text = 'Nombre del atributo',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_atributo.pack(
            fill='x',
            side='top')
        # txt USUSARIO
        txt_atributo = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_atributo.pack(
            fill='x',
            side='top')

        tk.Button(self,
                    text='Eliminar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=lambda: EliminarAtributo.delete_atributo(self,txt_atributo.get())).pack(side='top', fill='both',expand=True)

        tk.Button(self,
                    text='Cerrar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='top', fill='both',expand=True)
    def delete_atributo(self,nombre_atributo):
        try:
            AtributosController.eliminar_atributo(nombre_atributo)
            EliminarAtributo.open_EliminadoExitoso(self)
        except:
            EliminarAtributo.open_EliminadoError(self)
    def open_EliminadoExitoso(self):
           window = EliminadoExitoso(self)
           window.grab_set()
    def open_EliminadoError(self):
           window = EliminadoError(self)
           window.grab_set()  

# --- 0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 ---  0 --- 0 --- 
#Vistas de pop-up´s de estado
#SON VISTAS QUE INDICAN ALGUN EVENTO Y QUE SE PUEDEN USAR EN CUALQUIER MENU
class NoDisponibleView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('No disponible')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'No disponible',font = 'cooper 18', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        tk.Button(self,
                    text='Close',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='bottom', fill='both',expand=True)
class ContraseñaIncorrecta(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('350x100')
        self.title('Problema en login')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'La contraseña o el usuario son incorrectos,\no su usuario no esta habilitado',font = 'cooper 12', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        tk.Button(self,
                    text='Cerrar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='bottom', fill='both',expand=True)
class CargaExitosa(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Carga exitosa')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Carga exitosa',font = 'cooper 18', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        tk.Button(self,
                    text='Close',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='bottom', fill='both',expand=True)
class DesargaExitosa(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Descarga exitosa')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Descarga exitosa',font = 'cooper 18', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        tk.Button(self,
                    text='Close',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='bottom', fill='both',expand=True)         
class CargaError(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x180')
        self.title('Error en la carga')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Error en la carga.\nVuelva a intentarlo.',font = 'cooper 18', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        #Detalle = tk.Label(self, bg = 'white', text = 'Se creara un archivo .CSV\ncon la especificacion del error',font = 'cooper 12', fg = 'deep pink')
        #Detalle.pack(fill='both',side='top',expand=True)

        tk.Button(self,
                    text='Close',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='bottom', fill='both',expand=True)
class DescargaError(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x180')
        self.title('Error en la descarga')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Error en la descarga.\nVuelva a intentarlo.',font = 'cooper 18', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        Detalle = tk.Label(self, bg = 'white', text = 'Se creara un archivo .CSV\ncon la especificacion del error',font = 'cooper 12', fg = 'deep pink')
        Detalle.pack(fill='both',side='top',expand=True)

        tk.Button(self,
                    text='Close',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='bottom', fill='both',expand=True)

class EliminadoExitoso(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Eliminado exitoso')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Eliminado exitoso',font = 'cooper 18', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        tk.Button(self,
                    text='Close',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='bottom', fill='both',expand=True)
class EliminadoError(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x180')
        self.title('Error en el eliminado')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Error en el eliminado.\nVuelva a intentarlo.',font = 'cooper 18', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        #Detalle = tk.Label(self, bg = 'white', text = 'Se creara un archivo .CSV\ncon la especificacion del error',font = 'cooper 12', fg = 'deep pink')
        #Detalle.pack(fill='both',side='top',expand=True)

        tk.Button(self,
                    text='Close',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='bottom', fill='both',expand=True)




#Se crea clase principal (tk.Tk), la cual es la encargada de manejar los Frames
class APP(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.configure(bg = "white")

        self.title("Gestor de campañas")
        
        self.columnconfigure( 0, weight = 1 )
        self.rowconfigure(0, weight = 1)

        contenedor_principal = tk.Frame( self ,bg = "white")

        contenedor_principal.grid( padx = 40, pady = 50 , sticky = "nsew")

        self.todos_los_frames = dict()
        for F in (HomeView,Login, ContactosMenu, CampañasMenu, View_GestionarContactos,
                 View_GestionarAtributosClientes, View_ListasContactos,View_Campañas):

            frame = F( contenedor_principal , self)
            self.todos_los_frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame( Login )
    def show_frame(self,contenedor_llamado):
        frame = self.todos_los_frames[contenedor_llamado]
        frame.tkraise()

root = APP()
root.eval('tk::PlaceWindow . center')
root.mainloop()



### FALTA
# TERMINAR FRONT DE : CAMPAÑAS, LISTA CLIENTES, AGREGAR ATRIBUTOS A CLIENTES
# NAVEGACION ENTRE FRAMES

# TERMINAR BACK DE : LISTA CLIENTES, CAMPAÑAS
# TESTEAR 