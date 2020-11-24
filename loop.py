from tkinter import *
from tkinter import ttk
import calculator

botones = ('C', '+/-', '%', '÷', '7', '8', '9', 'x', '4', '5', '6', '-', '1', '2', '3', '+', '0', ',', '=')

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

        fila = 0
        tecla = 0
        for i in range (len(botones)):
            if fila < 5:
                for columna in range(4):
                    if tecla < 19:
                        if botones[tecla] == '0':
                            boton = calculator.CalcButton(self.teclado, botones[tecla])
                            boton.config(width=136)
                            boton.grid(row=fila, column=columna)
                        else:
                            boton = calculator.CalcButton(self.teclado, botones[tecla])
                            boton.grid(row=fila, column=columna)
                    tecla += 1
            fila+=1

if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
