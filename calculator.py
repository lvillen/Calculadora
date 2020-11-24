from tkinter import *
from tkinter import ttk

WIDTH = 68
HEIGHT = 50

botones = ('C', '+/-', '%', '÷', '7', '8', '9', 'x', '4', '5', '6', '-', '1', '2', '3', '+', '0', ',', '=')
dbotones = [
    {
        'text': 'C',
        'r': 0,
        'c': 1,
    },
    {
        'text': '+/-',
        'r': 0,
        'c': 2,
    },
    {
        'text': '÷',
        'r': 0,
        'c': 3,
    },
    {
        'text': '7',
        'r': 1,
        'c': 0,
    },
    {
        'text': '8',
        'r': 1,
        'c': 1,
    },
    {
        'text': '9',
        'r': 1,
        'c': 2,
    },
    {
        'text': 'x',
        'r': 1,
        'c': 3,
    },
    {
        'text': '4',
        'r': 2,
        'c': 0,
    },
    {
        'text': '5',
        'r': 2,
        'c': 1,
    },
    {
        'text': '6',
        'r': 2,
        'c': 2,
    },
    {
        'text': '-',
        'r': 2,
        'c': 3,
    },
    {
        'text': '1',
        'r': 3,
        'c': 0,
    },
    {
        'text': '2',
        'r': 3,
        'c': 1,
    },
    {
        'text': '3',
        'r': 3,
        'c': 2,
    },
    {
        'text': '+',
        'r': 3,
        'c': 3,
    },
    {
        'text':'0',
        'r':4,
        'c':0,
        'w': 2
    },
    {
        'text': ',',
        'r': 4,
        'c': 2,
    },
    {
        'text': '=',
        'r': 4,
        'c': 3,
    },
]

def retornaCaracter(tecla):
    print('Han pulsado ', tecla)

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

    def refresh(self, text):
        self.label.config(text=text)

class CalcButton(ttk.Frame):

    def __init__(self, parent, text, command=None, width=1, height=1):
        #Defino el cuadro sobre el que luego pintaré el objeto
        ttk.Frame.__init__(self, parent, width=WIDTH*width, height=HEIGHT*height)
        self.pack_propagate(0) #Para que mi tamaño mande
        
        #Defino el estilo para poder trabajar
        s = ttk.Style()
        s.theme_use('alt')

        #Como no voy a tener que recuperar los valores del botón, puedo hacerlo todo en una misma línea y sin definir variable
        ttk.Button(self, text=text, command=lambda: command(text)).pack(side=TOP, fill=BOTH, expand=True)

        #Defino el botón
        #btn = ttk.Button(self, text=text, command=command)
        #Empaquetado
        #btn.pack(side=TOP, fill=BOTH, expand=True)

'''
class Keyboard_sin_diccionario(ttk.Frame):

    def __init__(self, parent):
        #Defino el cuadro sobre el que luego pintaré el objeto
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*5)
        self.pack_propagate(0)

        #Defino el estilo para poder trabajar 'bien' porque 'aqua' no nos deja.
        s = ttk.Style()
        s.theme_use('alt')

        #Monto el bulce parte 1
        botones = (('C', 1), ('+/-',1), ('%',1), ('÷', 1), ('7', 1), ('8', 1), ('9', 1), ('x', 1), ('4', 1), ('5', 1), ('6', 1), ('-', 1), ('1', 1), ('2', 1), ('3', 1), ('+', 1), ('0',2), (',', 1), ('=', 1))
        coordenadas = []
        
        for fila in range(5):
            for columna in range(4):
                coordenadas.append((fila, columna))

        k=0
        valorAnt = ''
        for tecla, ancho in botones:
            boton = CalcButton(self, tecla, width=ancho)
            boton.grid(row=coordenadas[k][0], column=coordenadas[k][1], columnspan=ancho)
            k += ancho
'''

class Keyboard(ttk.Frame):
    def __init__(self, parent, command):        
        #Defino el cuadro sobre el que luego pintaré el objeto
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*5)
        self.pack_propagate(0)

        #Defino el estilo para poder trabajar 'bien' porque 'aqua' no nos deja.
        s = ttk.Style()
        s.theme_use('alt')

        for boton in dbotones:
            w = boton.get('w', 1)
                #if 'w' in boton:
                #w = boton['w']
            #else:
                #w = 1

            h = boton.get('h', 1)
                #if 'w' in boton:
                #h = boton['h']
            #else:
                #h = 1

            btn = CalcButton(self, boton['text'], width=w, height=h, command=command)
            btn.grid(row=boton['r'], column=boton['c'], columnspan=w, rowspan=h)

class Calculator(ttk.Frame):
    def __init__(self, parent):
        #Defino el cuadro sobre el que luego pintaré el objeto
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*6)
        self.pack_propagate(0)

        #Defino el estilo para poder trabajar 'bien' porque 'aqua' no nos deja.
        s = ttk.Style()
        s.theme_use('alt')

        self.display = calculator.Display(self)
        self.display.pack(side=TOP, fill=BOTH, expand=True)

        self.teclado = calculator.Keyboard(self, self.display.refresh) #Aquí será "self.gestiona_calculos"
        self.teclado.pack(side=TOP)

    def gestiona_calculos(self, tecla):
        '''
        Establecer toda la lógica de cálculos posibles en función de lo tecleado
        
        variables
            op1
            op2
            operación
            resultado
        '''

        pass