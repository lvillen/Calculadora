from tkinter import *
from tkinter import ttk

WIDTH = 68
HEIGHT = 50

class Display(ttk.Frame):

    def __init__(self, parent):
        #Defino el cuadro sobre el que luego pintaré el objeto
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT)
        self.pack_propagate(0)

        #Defino el estilo para poder trabajar 'bien' porque 'aqua' no nos deja.
        s = ttk.Style()
        s.theme_use('alt')

        #Defino la 'label'
        self.label = ttk.Label(self, text='0', anchor=E, background='black', foreground='white', font='Helvetica 36')
        #Empaquetado
        self.label.pack(side=TOP, fill=BOTH, expand=True)

class CalcButton(ttk.Frame):

    def __init__(self, parent, text, command=None, width=1, height=1):
        #Defino el cuadro sobre el que luego pintaré el objeto
        ttk.Frame.__init__(self, parent, width=WIDTH*width, height=HEIGHT*height)
        self.pack_propagate(0) #Para que mi tamaño mande
        
        #Defino el estilo para poder trabajar
        s = ttk.Style()
        s.theme_use('alt')

        #Como no voy a tener que recuperar los valores del botón, puedo hacerlo todo en una misma línea y sin definir variable
        ttk.Button(self, text=text, command=command).pack(side=TOP, fill=BOTH, expand=True)

        #Defino el botón
        #btn = ttk.Button(self, text=text, command=command)
        #Empaquetado
        #btn.pack(side=TOP, fill=BOTH, expand=True)


