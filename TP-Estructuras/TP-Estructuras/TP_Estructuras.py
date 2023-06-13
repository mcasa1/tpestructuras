import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from turtle import bgcolor
from Login import LoginController
from Atributos import AtributosController
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
        tk.Button(self,
                text='  Mails  ',
                bg = 'white',
                fg = 'deep pink',
                font = 'cooper 15',
                cursor='hand2',
                command=lambda: controller.show_frame( MailMenu )).pack(side='left',expand=True,fill='both')
  
#Sub menues
class ContactosMenu(tk.Frame):
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
                    command=lambda:controller.show_frame( GestionarContactos )).pack(side='left', fill='both',expand=True)       
        tk.Button(self,
                    text='Atributos',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( GestionarAtributosClientes )).pack(side='left', fill='both',expand=True)
        tk.Button(self,
                    text='Volver',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda:controller.show_frame( GestionarListasClientes )).pack(side='bottom', fill='x')
class MailMenu(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "white")

        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'GESTOR DE CLIENTES',font = 'cooper 25', fg = 'deep pink')
        titulo.pack(fill='both',side='top')

        tk.Button(self,
                    text='aaaaa',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( SubMenu2MainView )).pack(side='left', fill='both',expand=True)       
        tk.Button(self,
                    text='aaaaa',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( SubMenu2MainView )).pack(side='left', fill='both',expand=True)
        tk.Button(self,
                    text='Volver',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda:controller.show_frame( HomeView )).pack(side='bottom', fill='x')
class CampañasMenu(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "white")

        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'GESTOR DE CLIENTES',font = 'cooper 25', fg = 'deep pink')
        titulo.pack(fill='both',side='top')

        tk.Button(self,
                    text='aaaaa',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( SubMenu2MainView )).pack(side='left', fill='both',expand=True)       
        tk.Button(self,
                    text='aaaaa',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( SubMenu2MainView )).pack(side='left', fill='both',expand=True)
        tk.Button(self,
                    text='Volver',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda:controller.show_frame( HomeView )).pack(side='bottom', fill='x')

#MENUES 3ERA CAPA

# SUBCAPA GestorContactos
class GestionarContactos(tk.Frame):
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
class GestionarAtributosClientes(tk.Frame):
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
                    command=lambda: GestionarAtributosClientes.Eliminar_Atributo(self)).pack(side='bottom', fill='x')

        #BOTON AGREGAR ATRIBUTO
        tk.Button(self,
                    text='Agregar',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: GestionarAtributosClientes.Agregar_Atributo(self)).pack(side='bottom', fill='x')


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

        GestionarAtributosClientes.obtener_atributos(tree)

        #BOTON ACTUALIZAR
        tk.Button(self,
                    text='Actualizar',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: GestionarAtributosClientes.obtener_atributos(tree)).pack(side='bottom', fill='x')
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
class GestionarListasClientes(tk.Frame):
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

# SUBCAPA GestorMail

# SUBCAPA GestorCampañas

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
        for F in (HomeView,Login, ContactosMenu, MailMenu, CampañasMenu, GestionarContactos, GestionarAtributosClientes, GestionarListasClientes):

            frame = F( contenedor_principal , self)
            self.todos_los_frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame( Login )
    def show_frame(self,contenedor_llamado):
        frame = self.todos_los_frames[contenedor_llamado]
        frame.tkraise()
               
#1- Se crea APP como tal (aprovechandonos de la clase creada)
#2- Se centra la ventana en la pantalla
#3- Se ejecuta la ventana principal, creada a traves de POO con las clases respectivas

root = APP()
root.eval('tk::PlaceWindow . center')
root.mainloop()