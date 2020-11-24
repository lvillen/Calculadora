from tkinter import *
from tkinter import ttk
import calculator

def imprimeuno():
    print(1)

class MainApp(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        #self.geometry('272x300') No hace falta porque ya lo hemos definido con el tamaño de self.display y self.teclado
        self.title('Calculadora')

        self.display = calculator.Display(self)
        self.display.pack(side=TOP)

        self.teclado = ttk.Frame(self, width=calculator.WIDTH*4, height=calculator.HEIGHT*5)
        self.teclado.grid_propagate(0)
        self.teclado.pack(side=TOP, fill=BOTH, expand=True)

        botonC = calculator.CalcButton(self.teclado, 'C')
        botonC.grid(column=0, row=0)
        botonC = calculator.CalcButton(self.teclado, '+/-')
        botonC.grid(column=1, row=0)
        botonC = calculator.CalcButton(self.teclado, '%')
        botonC.grid(column=2, row=0)
        botonC = calculator.CalcButton(self.teclado, '÷')
        botonC.grid(column=3, row=0)

        botonC = calculator.CalcButton(self.teclado, '7')
        botonC.grid(column=0, row=1)
        botonC = calculator.CalcButton(self.teclado, '8')
        botonC.grid(column=1, row=1)
        botonC = calculator.CalcButton(self.teclado, '9')
        botonC.grid(column=2, row=1)
        botonC = calculator.CalcButton(self.teclado, 'x')
        botonC.grid(column=3, row=1)

        botonC = calculator.CalcButton(self.teclado, '4')
        botonC.grid(column=0, row=2)
        botonC = calculator.CalcButton(self.teclado, '5')
        botonC.grid(column=1, row=2)
        botonC = calculator.CalcButton(self.teclado, '6')
        botonC.grid(column=2, row=2)
        botonC = calculator.CalcButton(self.teclado, '-')
        botonC.grid(column=3, row=2)

        botonC = calculator.CalcButton(self.teclado, '1')
        botonC.grid(column=0, row=3)
        botonC = calculator.CalcButton(self.teclado, '2')
        botonC.grid(column=1, row=3)
        botonC = calculator.CalcButton(self.teclado, '3')
        botonC.grid(column=2, row=3)
        botonC = calculator.CalcButton(self.teclado, '+')
        botonC.grid(column=3, row=3)

        botonC = calculator.CalcButton(self.teclado, '0')
        botonC.grid(column=0, row=4)
        #botonC = calculator.CalcButton(self.teclado, '0')
        #botonC.grid(column=1, row=4)
        botonC = calculator.CalcButton(self.teclado, ',')
        botonC.grid(column=2, row=4)
        botonC = calculator.CalcButton(self.teclado, '=')
        botonC.grid(column=3, row=4)


#TERMINAR DE MONTAR LA CALCULADORA
#PENSAR QUÉ BUCLE PODEMOS MONTAR, INFORMANDO DE CADA BOTÓN (Diccionario, lista...)

        '''
        self.calcButtonC = ttk.Frame(self, width=136, height=50)
        btn = ttk.Button(self.calcButtonC, text='C')
        self.calcButtonC.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)
        self.calcButtonC.grid(column=0, row=1, columnspan=2)

        self.calcButtonCs = ttk.Frame(self, width=68, height=50)
        btn = ttk.Button(self.calcButtonCs, text='+/-')
        self.calcButtonCs.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)
        self.calcButtonCs.grid(column=2, row=1)

        self.calcButtondiv = ttk.Frame(self, width=68, height=50)
        btn = ttk.Button(self.calcButtondiv, text='÷')
        self.calcButtondiv.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)
        self.calcButtondiv.grid(column=3, row=1)

        #self.mainloop() Esto tiene que ir siempre al final
        '''



if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
