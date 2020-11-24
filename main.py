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
    
    def procesa(self, tecla):
        #<Toda la lógica de cálculo>
        #if tecla es numero -> pon el número en el display
        #if tecla es + -> procesa la suma
        #if teclas es * -> procesa la multiplicación
        #if tecla es / -> procesa la división

if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
