import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
from tkinter.filedialog import asksaveasfilename
from tkcalendar import Calendar
from tktimepicker import SpinTimePickerModern,constants
from datetime import *

from Login import LoginController
from Atributos import AtributosController
from Contacto import Contacto_Controller, Contacto
from campana import CampañaController, Campaña
from ListaContactos import ListaContactosController, ListaContactos


class tkinterStyles():
    #Clase con estilos que se usan para los widgets de tkinter
    def estiloTabla():
        # Estilo para una tabla con el widget treeview
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('cooper', 11)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('cooper', 13,'bold')) # Modify the font of the headings
        #style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        return style

### -------------------------------------------------- VISTAS -------------------------------------------------- ###

### ---------------------------------------------------------- VISTA DEL LOGIN --------------------------------- ###
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
            
### ---------------------------------------------------------- VISTA DEL HOME VIEW ----------------------------- ###

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
 
### ---------------------------------------------------------- VISTAS DE SUBMENUES ----------------------------- ###

### ------------------------------------------------------------------------- SUBMENU CONTACTOS ---------------- ###
class ContactosMenu(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "white")

        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Menu Contactos',font = 'cooper 25', fg = 'deep pink')
        titulo.pack(fill='both',side='top')

        tk.Button(self,
                    text='Volver',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda:controller.show_frame( HomeView )).pack(side='bottom', fill='x')
        tk.Button(self,
                    text='      Contactos      ',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( View_GestionarContactos )).pack(side='left', fill='both',expand=True)       
        tk.Button(self,
                    text='      Atributos      ',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( View_GestionarAtributosClientes )).pack(side='left', fill='both',expand=True)
        tk.Button(self,
                    text='Atributos a contactos',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( View_AgregarAtributosAClientes )).pack(side='left', fill='both',expand=True)
### ------------------------------------------------------------------------- SUBMENU CAMPAÑAS ----------------- ###
class CampañasMenu(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "white")

        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'GESTOR DE CAMPAÑAS',font = 'cooper 25', fg = 'deep pink')
        titulo.pack(fill='both',side='top')

        tk.Button(self,
                    text='     Campañas    ',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( View_Campañas )).pack(side='left', fill='both',expand=True)       
        tk.Button(self,
                    text='Listas de contactos',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 15',
                    cursor='hand2',
                    command=lambda:controller.show_frame( View_GestionarListasContactos )).pack(side='left', fill='both',expand=True)
        tk.Button(self,
                    text='Volver',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda:controller.show_frame( HomeView )).pack(side='bottom', fill='x')

### ---------------------------------------------------------- VISTAS DE 3ER CAPA MENUES ----------------------- ###

### ------------------------------------------------------------------------- CONTACTOS VIEW ------------------- ###
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

        #BOTON IMPORTAR CONTACTOS
        tk.Button(self,
                    text='Importar contactos',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_GestionarContactos.importarContactos(self)).pack(side='bottom', fill='x')

        #BOTON AGREGAR CONTACTO
        tk.Button(self,
                    text='Agregar',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_GestionarContactos.Agregar_Contacto(self)).pack(side='bottom', fill='x')

        #BOTON BUSCAR CONTACTOS
        tk.Button(self,
                text='Buscar',
                bg = 'white',
                fg = 'deep pink',
                font = 'cooper 10',
                cursor='hand2',
                command=lambda: View_GestionarContactos.buscar_contactos(self)).pack(side='bottom', fill='x')


        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Contactos',font = 'cooper 25', fg = 'deep pink')
        titulo.pack(fill='both',side='top')
        espacio = tk.Label(self, bg = 'white', text = '  ',font = 'cooper 25', fg = 'deep pink')
        espacio.pack(fill='both',side='top')


        # TREEVIEW PARA MOSTRAR LOS DATOS

        #CONFIGURACION DE LA TABLA
        tkinterStyles.estiloTabla()
        tree = ttk.Treeview(self,show='headings', columns=['ID_CONTACTO','NOMBRE_CONTACTO','FECHA_NACIMIENTO','EMAIL','DIRECCION','SEXO'], style= "mystyle.Treeview")
                #COLUMNAS DEL TREEVIEW
        tree.heading('ID_CONTACTO', text='ID CONTACTO')
        tree.heading('NOMBRE_CONTACTO', text='NOMBRE')
        tree.heading('FECHA_NACIMIENTO', text='NACIMIENTO')
        tree.heading('EMAIL', text='EMAIL')
        tree.heading('DIRECCION', text='DIRECCION')
        tree.heading('SEXO', text='SEXO')

        #SCROLLBAR PARA EL TREEVIEW
        verscrlbar = ttk.Scrollbar(self,
                                   #orient ="vertical",
                                   command = tree.yview)
        # CONFIGURACION DE LA SCROLLBAR
        tree.configure(yscrollcommand = verscrlbar.set)
        verscrlbar.pack(side ='right', fill ='y')
        tree.pack(side='top', fill='both')         

        #LLENADO DE DATOS
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
    def Agregar_Contacto(self):
        window = AgregarContacto(self)
        window.grab_set()
    def Eliminar_Contacto(self):
        window = EliminarContacto(self)
        window.grab_set() 
    def importarContactos(self):
        window = importarContactos(self)
        window.grab_set() 
    def buscar_contactos(self):
        window = Buscar_Contactos(self)
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
class importarContactos(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x180')
        self.title('Importacion de contactos')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Importar contactos',font = 'cooper 16', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)
        tk.Button(self,
                    text='Descargar plantilla',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=lambda: importarContactos.descargarPlantilla(self)).pack(side='top', fill='both',expand=True)

        tk.Button(self,
                    text='Cargar datos',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=lambda: importarContactos.procesarContactos(self)).pack(side='top', fill='both',expand=True)

        tk.Button(self,
                    text='Cerrar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='top', fill='both',expand=True)
    def descargarPlantilla(self):
        try:
            #create path to save a .xlsx file with tkinter
            data = [("xlsx file(*.xlsx)","*.xlsx")]
            path = asksaveasfilename(filetypes = data, defaultextension = data)
            Contacto_Controller.importacionMasivaPlantilla(path)
            importarContactos.open_DescargaExitosa(self)
        except:
            importarContactos.open_DescargaError(self)
    def procesarContactos(self): 
        try:
            file = filedialog.askopenfilename()
            filasErrores, contadorProcesadas = Contacto_Controller.importacionMasivaProcesamiento(file)
            messagebox.showinfo(message= contadorProcesadas, title="Filas procesadas")
            if len(filasErrores) > 0:
                messagebox.showinfo(message=filasErrores, title="Filas que no pudieron ser procesadas")
            importarContactos.open_CargaExitosa(self)
        except:
            importarContactos.open_CargaError(self)

    def open_CargaExitosa(self):
           window = CargaExitosa(self)
           window.grab_set()
    def open_CargaError(self):
           window = CargaError(self)
           window.grab_set()  
    def open_DescargaExitosa(self): 
           window = DesargaExitosa(self)
           window.grab_set()
    def open_DescargaError(self):
           window = DescargaError(self)
           window.grab_set()  
class Buscar_Contactos(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.geometry('1275x680')
        self.title('Buscar contactos')
        
        mi_canvas = tk.Canvas(self)
        mi_canvas.pack(side='left', fill='both', expand=True)
        
        mi_scrollbar = ttk.Scrollbar(self, orient='vertical', command=mi_canvas.yview)
        mi_scrollbar.pack(side='right', fill='y')
        
        mi_canvas.configure(yscrollcommand=mi_scrollbar.set)
        mi_canvas.bind('<Configure>', lambda e: mi_canvas.configure(scrollregion = mi_canvas.bbox('all')))
        
        segundo_frame = tk.Frame(mi_canvas)
        
        mi_canvas.create_window((0,0), window=segundo_frame, anchor='nw')
        
        #LABEL TITULO
        titulo = tk.Label(segundo_frame, bg = 'white', text = 'Buscar contactos',font = 'cooper 16', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)
        
        # LABEL ID_CONTACTO
        titulo_id_contacto = tk.Label(segundo_frame, pady = 5, bg = 'white', text = 'ID Contacto',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_id_contacto.pack(
            fill='x',
            side='top')
        # ENTRY NOMBRE
        txt_id_contacto = tk.Entry(segundo_frame, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_id_contacto.pack(
            fill='x',
            side='top')
        
        # LABEL NOMBRE
        titulo_nombre = tk.Label(segundo_frame, pady = 5, bg = 'white', text = 'Nombre y apellido',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_nombre.pack(
            fill='x',
            side='top')
        # ENTRY NOMBRE
        txt_nombre = tk.Entry(segundo_frame, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_nombre.pack(
            fill='x',
            side='top')


        # LABEL MAIL
        titulo_mail = tk.Label(segundo_frame, pady = 5, bg = 'white', text = 'E-mail',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_mail.pack(
            fill='x',
            side='top')
        # ENTRY MAIL
        txt_mail= tk.Entry(segundo_frame, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_mail.pack(
            fill='x',
            side='top')

        # EDAD_DESDE
        titulo_edad_desde= tk.Label(segundo_frame, pady = 5, bg = 'white', text = 'Edad Desde',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_edad_desde.pack(
            fill='x',
            side='top')
        # ENTRY EDAD_DESDE
        txt_edad_desde= tk.Entry(segundo_frame, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_edad_desde.pack(
            fill='x',
            side='top')
        
        # EDAD_HASTA
        titulo_edad_hasta= tk.Label(segundo_frame, pady = 5, bg = 'white', text = 'Edad hasta',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_edad_hasta.pack(
            fill='x',
            side='top')
        # ENTRY EDAD_HASTA
        txt_edad_hasta= tk.Entry(segundo_frame, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_edad_hasta.pack(
            fill='x',
            side='top')
        
        # LABEL DIRECCION
        titulo_direccion= tk.Label(segundo_frame, pady = 5, bg = 'white', text = 'Dirección',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_direccion.pack(
            fill='x',
            side='top')
        # ENTRY DIRECCION
        txt_direccion= tk.Entry(segundo_frame, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_direccion.pack(
            fill='x',
            side='top')

        # LABEL SEXO
        titulo_sexo= tk.Label(segundo_frame, pady = 5, bg = 'white', text = 'Sexo',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_sexo.pack(
            fill='x',
            side='top')
        # ENTRY SEXO
        sexo_box = ttk.Combobox(segundo_frame,
            state="readonly",
            values=['',"Masculino", "Femenino"])

        sexo_box.current(0)
        sexo_box.pack(side='top', fill='both',expand=True)

        # LABEL ATRIBUTOS
        titulo_atributos= tk.Label(segundo_frame, pady = 5, bg = 'white', text = 'Atributos (Se puede ingresar varios separando con ",")',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_atributos.pack(
            fill='x',
            side='top')
        # ENTRY ATRIBUTOS
        txt_atributos= tk.Entry(segundo_frame, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_atributos.pack(
            fill='x',
            side='top')

        #CONFIGURACION DE LA TABLA
        tkinterStyles.estiloTabla()

        tree = ttk.Treeview(segundo_frame, show='headings', columns=['ID_CONTACTO','NOMBRE_CONTACTO','FECHA_NACIMIENTO','EMAIL','DIRECCION','SEXO'], style= "mystyle.Treeview")
        tree.heading('ID_CONTACTO', text='ID CONTACTO')
        tree.heading('NOMBRE_CONTACTO', text='NOMBRE')
        tree.heading('FECHA_NACIMIENTO', text='NACIMIENTO')
        tree.heading('EMAIL', text='EMAIL')
        tree.heading('DIRECCION', text='DIRECCION')
        tree.heading('SEXO', text='SEXO')

        #SCROLLBAR PARA EL TREEVIEW
        verscrlbar = ttk.Scrollbar(segundo_frame,
                                   #orient ="vertical",
                                   command = tree.yview)
        # CONFIGURACION DE LA SCROLLBAR
        tree.configure(yscrollcommand = verscrlbar.set)
        verscrlbar.pack(side ='right', fill ='y')
        tree.pack(side='top', fill='both')

        tree.pack(side='right', fill='both')

        tk.Button(segundo_frame,
                text='Filtrar',
                cursor='hand2',
                bg = 'white',
                fg = 'deep pink',
                command=lambda: Buscar_Contactos.buscar_contactos(self,tree,
                                                                 txt_id_contacto.get(),
                                                                txt_nombre.get(),
                                                               txt_mail.get(),
                                                             txt_edad_desde.get(),
                                                            txt_edad_hasta.get(),
                                                           txt_direccion.get(),
                                                          sexo_box.get(),
                                                         txt_atributos.get()
                                                         )
                ).pack(side='top', fill='both',expand=True)

        tk.Button(segundo_frame,
                    text='Cerrar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='bottom', fill='both',expand=True)
        
    def buscar_contactos(self,tree,id_contacto,nombre,email,edad_desde, edad_hasta, direccion, sexo, atributo):

        if id_contacto == '':
            id_contacto = None
        if nombre == '':
            nombre = None
        if email == '':
            email = None
        if edad_desde == '':
            edad_desde = None
        if edad_hasta == '':
            edad_hasta = None
        if direccion == '':
            direccion = None
        if sexo == '':
            sexo = None
        
        atributo = atributo.split(',')
        atributo = [x.strip(' ') for x in atributo]
        
        if atributo == ['']:
            atributo = []
        
        list_contactos2 = Contacto_Controller.obtener_contactos_params(id_contacto=id_contacto, nombre=nombre,email=email,edad_desde=edad_desde, edad_hasta=edad_hasta, direccion=direccion, sexo=sexo, atributo=atributo, habilitado=1)

        for i in tree.get_children():
            tree.delete(i)

        for contacto in list_contactos2:
            tree.insert('',tk.END ,values=[contacto.id_contacto,contacto.nombre,contacto.fecha_nacimiento,contacto.email,contacto.direccion,contacto.sexo])

### ------------------------------------------------------------------------- ATRIBUTOS VIEW ------------------- ###
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

        #BOTON AGREGAR CONTACTO
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

### ------------------------------------------------------------------------- ASIGNAR ATRIBUTOS VIEW ----------- ###

class View_AgregarAtributosAClientes(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "white")

        #BOTON VOLVER
        btn_volver = tk.Button(self,
                    text='Volver',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda:controller.show_frame( ContactosMenu ))

        btn_delete = tk.Button(self,
                    text='Eliminar asignacion de atributo',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_AgregarAtributosAClientes.EliminarAtributoContacto(self))

        btn_add =tk.Button(self,
                    text='Asignar atributo a un contacto',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_AgregarAtributosAClientes.AsignarAtributoContacto(self))

        #BOTON ACTUALIZAR
        btn_updt = tk.Button(self,
                    text='Actualizar',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_AgregarAtributosAClientes.actualizarTablas(tree_atributos,tree_contactos))

        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Asignar atributos',font = 'cooper 25', fg = 'deep pink')
        espacio = tk.Label(self, bg = 'white', text = '  ',font = 'cooper 25', fg = 'deep pink')

        # ----------------------------  TABLA DE ATRIBUTOS ----------------------------  

        #CONFIGURACION DE LA TABLA
        tkinterStyles.estiloTabla()

        tree_atributos = ttk.Treeview(self, show='headings', columns=['ID_ATRIBUTO','ATRIBUTO_DESCRIPCION'], style= "mystyle.Treeview")
        tree_atributos.heading('ID_ATRIBUTO', text='ID DE ATRIBUTO')
        tree_atributos.heading('ATRIBUTO_DESCRIPCION', text='DESCRIPCION')

        #SCROLLBAR PARA EL TREEVIEW
        tree_atributos_verscrlbar = ttk.Scrollbar(self,
                                   #orient ="vertical",
                                   command = tree_atributos.yview)
        # CONFIGURACION DE LA SCROLLBAR
        tree_atributos.configure(yscrollcommand = tree_atributos_verscrlbar.set)

        # ----------------------------  TABLA DE CONTACTOS ----------------------------  

        #CONFIGURACION DE LA TABLA
        tree_contactos = ttk.Treeview(self,show='headings', columns=['ID_CONTACTO','NOMBRE_CONTACTO','EMAIL','ATRIBUTOS'], style= "mystyle.Treeview")
                #COLUMNAS DEL TREEVIEW
        tree_contactos.heading('ID_CONTACTO', text='ID CONTACTO')
        tree_contactos.heading('NOMBRE_CONTACTO', text='NOMBRE')
        tree_contactos.heading('EMAIL', text='EMAIL')
        tree_contactos.heading('ATRIBUTOS', text='ATRIBUTOS')

        #SCROLLBAR PARA EL TREEVIEW
        tree_contactos_verscrlbar = ttk.Scrollbar(self,
                                   #orient ="vertical",
                                   command = tree_contactos.yview)
        # CONFIGURACION DE LA SCROLLBAR
        tree_contactos.configure(yscrollcommand = tree_contactos_verscrlbar.set)

        # ----------------------------  TABLA DE CONTACTOS ----------------------------  
        View_AgregarAtributosAClientes.actualizarTablas(tree_atributos,tree_contactos)


        # ----------------------------       .PACK        ----------------------------
        titulo.pack(fill='both',side='top')
        espacio.pack(fill='both',side='top')

        btn_volver.pack(side='bottom', fill='x')
        btn_delete.pack(side='bottom', fill='x')
        btn_add.pack(side='bottom', fill='x')
        btn_updt.pack(side='bottom', fill='x')


        tree_contactos.pack(side='left', fill='both')         
        tree_contactos_verscrlbar.pack(side ='left', fill ='y')

        tree_atributos.pack(side='left', fill='both') 
        tree_atributos_verscrlbar.pack(side ='left', fill ='y')
    def obtener_contactos(tree):
        pass
        for i in tree.get_children():
            tree.delete(i)
        dict_contactos = Contacto_Controller.obtener_contactos_atributos(habilitado=1)

        for key, contacto in dict_contactos.items():
            tree.insert('',tk.END ,values=[key,contacto.nombre,contacto.email, list(contacto.atributos.values())])
    def obtener_atributos(tree):
        for i in tree.get_children():
            tree.delete(i)
        lista_atributos = AtributosController.obtener_atributos()

        for row in lista_atributos:
            tree.insert('',tk.END ,values=[row.ID_atributo,row.AtributoDescripcion])
    def actualizarTablas(tree_atributos, tree_contactos):
        View_AgregarAtributosAClientes.obtener_atributos(tree_atributos)
        View_AgregarAtributosAClientes.obtener_contactos(tree_contactos)
    def AsignarAtributoContacto(self):
        window = AsignarAtributoContacto(self)
        window.grab_set()
    def EliminarAtributoContacto(self):
        window = EliminarAtributoContacto(self)
        window.grab_set()         
class AsignarAtributoContacto(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x240')
        self.title('Asignar atributo')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Asignar un atributo a un contacto',font = 'cooper 16', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        # LABEL CONTACTO
        titulo_contacto = tk.Label(self, pady = 5, bg = 'white', text = 'ID del contacto',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_contacto.pack(
            fill='x',
            side='top')
        # txt USUSARIO
        txt_contacto = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_contacto.pack(
            fill='x',
            side='top')

        # LABEL ATRIBUTO
        titulo_atributo = tk.Label(self, pady = 5, bg = 'white', text = 'ID del atributo',font = 'cooper 12', fg = 'deep pink', justify = 'left')
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
                    command=lambda: AsignarAtributoContacto.postContactoAtributo(self,txt_contacto.get(),txt_atributo.get())).pack(side='top', fill='both',expand=True)

        tk.Button(self,
                    text='Cerrar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='top', fill='both',expand=True)
    def postContactoAtributo(self,id_contacto, id_atributo):
        try:
            newContactAtribute = Contacto(id_contacto=id_contacto,atributos={id_atributo:None})
            Contacto_Controller.agregar_atributos_contacto(newContactAtribute)
            AsignarAtributoContacto.open_CargaExitosa(self)
        except:
            AsignarAtributoContacto.open_CargaError(self)
    def open_CargaExitosa(self):
           window = CargaExitosa(self)
           window.grab_set()
    def open_CargaError(self):
           window = CargaError(self)
           window.grab_set()    
class EliminarAtributoContacto(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x240')
        self.title('Eliminar atributo')

                #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Desasignar un atributo a un contacto',font = 'cooper 16', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        # LABEL CONTACTO
        titulo_contacto = tk.Label(self, pady = 5, bg = 'white', text = 'ID del contacto',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_contacto.pack(
            fill='x',
            side='top')
        # txt USUSARIO
        txt_contacto = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_contacto.pack(
            fill='x',
            side='top')

        # LABEL ATRIBUTO
        titulo_atributo = tk.Label(self, pady = 5, bg = 'white', text = 'ID del atributo',font = 'cooper 12', fg = 'deep pink', justify = 'left')
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
                    command=lambda: EliminarAtributoContacto.deleteContactoAtributo(self,txt_contacto.get(),txt_atributo.get())).pack(side='top', fill='both',expand=True)

        tk.Button(self,
                    text='Cerrar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='top', fill='both',expand=True)
    def deleteContactoAtributo(self,id_contacto, id_atributo):
        try:
            newContactAtribute = Contacto(id_contacto=id_contacto,atributos={id_atributo:None})
            Contacto_Controller.eliminar_atributos_contacto(newContactAtribute)
            EliminarAtributoContacto.open_EliminadoExitoso(self)
        except:
            EliminarAtributoContacto.open_EliminadoError(self)
    def open_EliminadoExitoso(self):
           window = EliminadoExitoso(self)
           window.grab_set()
    def open_EliminadoError(self):
           window = EliminadoError(self)
           window.grab_set()  

### ------------------------------------------------------------------------- LISTAS DE CONTACTOS VIEW --------- ###

# LISTA DE CONTACTOS
# VISTAS Y POP-UPs DE LISTAS DE CONTACTOS
class View_GestionarListasContactos(tk.Frame):
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
                    command=lambda:controller.show_frame( CampañasMenu )).pack(side='bottom', fill='x')

        #BOTON ELIMINAR
        tk.Button(self,
                    text='Eliminar una lista',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_GestionarContactos.Eliminar_Contacto(self)).pack(side='bottom', fill='x')

        #BOTON CREAR LISTA
        tk.Button(self,
                    text='Crear una lista',
                    bg = 'white',
                    fg = 'deep pink',
                    font = 'cooper 10',
                    cursor='hand2',
                    command=lambda: View_GestionarListasContactos.crear_lista_contacto(self)).pack(side='bottom', fill='x')
        
        #BOTON AGREGAR CONTACTOS 
        tk.Button(self,
                text='Agregar contactos a una lista',
                bg = 'white',
                fg = 'deep pink',
                font = 'cooper 10',
                cursor='hand2',
                command=lambda: View_GestionarListasContactos.agregar_contactos(self)).pack(side='bottom', fill='x')
        
        #BOTON AGREGAR CONTACTOS 
        tk.Button(self,
                text='Actualizar',
                bg = 'white',
                fg = 'deep pink',
                font = 'cooper 10',
                cursor='hand2',
                command=lambda: View_GestionarListasContactos.actualizar(tree,tree2)).pack(side='bottom', fill='x')


        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Lista de contactos',font = 'cooper 25', fg = 'deep pink')
        titulo.pack(fill='both',side='top')
        espacio = tk.Label(self, bg = 'white', text = '  ',font = 'cooper 25', fg = 'deep pink')
        espacio.pack(fill='both',side='top')

        #CONFIGURACION DE LA TABLA
        tkinterStyles.estiloTabla()

        tree = ttk.Treeview(self, show='headings', columns=['ID_LISTA_CONTACTOS','NOMBRE_LISTA_CONTACTOS', 'DESCRIPCION_LISTA_CONTACTOS'], style= "mystyle.Treeview")
        tree.heading('ID_LISTA_CONTACTOS', text='ID LISTA CONTACTOS')
        tree.heading('NOMBRE_LISTA_CONTACTOS', text='NOMBRE')
        tree.heading('DESCRIPCION_LISTA_CONTACTOS', text='DESCRIPCION')    
    
        View_GestionarListasContactos.obtener_listas_contactos(tree)
        
        tree2 = ttk.Treeview(self, show='headings', columns=['ID_CONTACTO','EMAIL_CONTACTO', 'ID_LISTA_CONTACTOS'], style= "mystyle.Treeview")
        tree2.heading('ID_CONTACTO', text='ID CONTACTO')
        tree2.heading('EMAIL_CONTACTO', text='EMAIL CONTACTO')
        tree2.heading('ID_LISTA_CONTACTOS', text='ID LISTA CONTACTOS')
        
        View_GestionarListasContactos.obtener_listas_contactos_contactos(tree2)

    def obtener_listas_contactos(tree):
        for i in tree.get_children():
            tree.delete(i)
        lista_contactos = ListaContactosController.obtener_lista_contactos_datos()

        for listac in lista_contactos:
            tree.insert('',tk.END ,values=[listac.ID_lista_contactos,listac.nombre_lista_contacto,listac.descripcion_lista_contacto])
            tree.pack(side='left', fill='both')
    
    def obtener_listas_contactos_contactos(tree2):
        for i in tree2.get_children():
            tree2.delete(i)
        lista_contactos = ListaContactosController.obtener_lista_contactos_contactos()

        for listac in lista_contactos:
            for contactos in listac.Contactos:
                tree2.insert('',tk.END ,values=[contactos.id_contacto,contactos.email,listac.ID_lista_contactos])
                tree2.pack(side='left', fill='both')
    
    def actualizar(tree, tree2):
        View_GestionarListasContactos.obtener_listas_contactos(tree)
        View_GestionarListasContactos.obtener_listas_contactos_contactos(tree2)
    

    def crear_lista_contacto(self):
        window = CrearListaContactos(self)
        window.grab_set()
    def agregar_contactos(self):
        window = AgregarContactosLista(self)
        window.grab_set()
    def Eliminar_Contacto(self):
        window = EliminarContacto(self)
        window.grab_set()   
class CrearListaContactos(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('600x420')
        self.title('Crear lista de contactos')

        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Crear una lista de contactos',font = 'cooper 16', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        # LABEL NOMBRE
        titulo_nombre_lista = tk.Label(self, pady = 5, bg = 'white', text = 'Nombre',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_nombre_lista.pack(
            fill='x',
            side='top')
        # ENTRY NOMBRE
        txt_nombre_lista = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_nombre_lista.pack(
            fill='x',
            side='top')


        # LABEL DESCRIPCION
        titulo_descripcion_lista = tk.Label(self, pady = 5, bg = 'white', text = 'Descripcion',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_descripcion_lista.pack(
            fill='x',
            side='top')
        # ENTRY DESCRIPCION
        txt_descripcion_lista= tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_descripcion_lista.pack(
            fill='x',
            side='top')


        tk.Button(self,
                    text='Crear',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=lambda: CrearListaContactos.post_lista(self,
                                                                txt_nombre_lista.get(),
                                                               txt_descripcion_lista.get(),   
                                                               )
                   ).pack(side='top', fill='both',expand=True)

        tk.Button(self,
                    text='Cerrar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='top', fill='both',expand=True)
        
    def post_lista(self,nombre,descripcion):
            nueva_lista = ListaContactos(nombre_lista_contacto=nombre, descripcion_lista_contacto=descripcion)
            ListaContactosController.crear_lista_contactos(nueva_lista)
class AgregarContactosLista(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.geometry('400x520')
        self.title('Agregar contactos lista')

        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Agregar contactos a una lista',font = 'cooper 16', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)
        
         # LABEL ID LISTA CONTACTO
        titulo_ID_lista_contacto = tk.Label(self, pady = 5, bg = 'white', text = 'ID Lista contacto',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_ID_lista_contacto.pack(
            fill='x',
            side='top')
        # ENTRY ID LISTA CONTACTO
        txt_ID_lista_contacto = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_ID_lista_contacto.pack(
            fill='x',
            side='top')
        
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

        # EDAD_DESDE
        titulo_edad_desde= tk.Label(self, pady = 5, bg = 'white', text = 'Edad Desde',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_edad_desde.pack(
            fill='x',
            side='top')
        # ENTRY EDAD_DESDE
        txt_edad_desde= tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_edad_desde.pack(
            fill='x',
            side='top')
        
        # EDAD_HASTA
        titulo_edad_hasta= tk.Label(self, pady = 5, bg = 'white', text = 'Edad hasta',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_edad_hasta.pack(
            fill='x',
            side='top')
        # ENTRY EDAD_HASTA
        txt_edad_hasta= tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_edad_hasta.pack(
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
            values=['',"Masculino", "Femenino"])

        sexo_box.current(0)
        sexo_box.pack(side='top', fill='both',expand=True)

        # LABEL ATRIBUTOS
        titulo_atributos= tk.Label(self, pady = 5, bg = 'white', text = 'Atributos (Se puede ingresar varios separando con ",")',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_atributos.pack(
            fill='x',
            side='top')
        # ENTRY ATRIBUTOS
        txt_atributos= tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_atributos.pack(
            fill='x',
            side='top')

        tk.Button(self,
                text='Agregar',
                cursor='hand2',
                bg = 'white',
                fg = 'deep pink',
                command=lambda: AgregarContactosLista.buscar_contactos(self,
                                                                 txt_ID_lista_contacto.get(),
                                                                txt_nombre.get(),
                                                              txt_edad_desde.get(),
                                                             txt_edad_hasta.get(),
                                                            sexo_box.get(),
                                                           txt_atributos.get()
                                                           )
                ).pack(side='top', fill='both',expand=True)

        tk.Button(self,
                    text='Cerrar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='bottom', fill='both',expand=True)
    
    def buscar_contactos(self,ID_lista_contactos,nombre,edad_desde,edad_hasta,sexo,atributo):
        
        if nombre == '':
            nombre = None
        if edad_desde == '':
            edad_desde = None
        if edad_hasta == '':
            edad_hasta = None
        if sexo == '':
            sexo = None
        
        atributo = atributo.split(',')
        atributo = [x.strip(' ') for x in atributo]
        
        if atributo == ['']:
            atributo = []
        
        list_contactos2 = Contacto_Controller.obtener_contactos_params(nombre=nombre,edad_desde=edad_desde, edad_hasta=edad_hasta, sexo=sexo, atributo=atributo, habilitado=1)
        
        
        lista_de_contactos = ListaContactos(ID_lista_contactos=ID_lista_contactos,lista_contactos=list_contactos2)
        
        AgregarContactosLista.insertar_contactos(lista_de_contactos)
        
    def insertar_contactos(lista_de_contactos):
        ListaContactosController.agregarContactos(lista_de_contactos)

### ------------------------------------------------------------------------- CAMPAÑAS VIEW -------------------- ###

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
                    command=lambda:controller.show_frame( CampañasMenu )).pack(side='bottom', fill='x')

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
        self.title('Eliminar campaña')

        #LABEL TITULO
        titulo = tk.Label(self, bg = 'white', text = 'Eliminar una campaña',font = 'cooper 16', fg = 'deep pink')
        titulo.pack(fill='both',side='top',expand=True)

        # LABEL USUSARIO
        titulo_campaña = tk.Label(self, pady = 5, bg = 'white', text = 'ID de la campaña',font = 'cooper 12', fg = 'deep pink', justify = 'left')
        titulo_campaña.pack(
            fill='x',
            side='top')
        # txt USUSARIO
        txt_campaña = tk.Entry(self, bg = 'white',font = 'cooper 10', fg = 'deep pink')
        txt_campaña.pack(
            fill='x',
            side='top')

        tk.Button(self,
                    text='Eliminar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=lambda: EliminarCampaña.delete_campaña(self,txt_campaña.get())).pack(side='top', fill='both',expand=True)

        tk.Button(self,
                    text='Cerrar',
                    cursor='hand2',
                    bg = 'white',
                    fg = 'deep pink',
                    command=self.destroy).pack(side='top', fill='both',expand=True)
    def delete_campaña(self,id_campaña):
        try:
            int(id_campaña)
            CampañaController.eliminar_campaña(id_campaña)
            EliminarCampaña.open_EliminadoExitoso(self)
        except ValueError:
            messagebox.showinfo(message="Ingrese un ID valido", title="Error en la entrada")
        except Exception:
            EliminarCampaña.open_EliminadoError(self)
    def open_EliminadoExitoso(self):
           window = EliminadoExitoso(self)
           window.grab_set()
    def open_EliminadoError(self):
           window = EliminadoError(self)
           window.grab_set()  

### ---------------------------------------------------------- VISTAS DE POP-UPS ------------------------------- ###
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

### -------------------------------------------------- APP MAIN ------------------------------------------------ ###
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
                 View_GestionarAtributosClientes, View_GestionarListasContactos,View_Campañas,View_AgregarAtributosAClientes):

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