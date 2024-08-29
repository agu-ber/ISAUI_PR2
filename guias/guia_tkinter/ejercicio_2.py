# Escribir una aplicación GUI (llamada ContDecreciente) como la que se
# ve en la figura. Cada ves que se haga clic en el botón "-", al valor de
# contador se le resta 1. El programa lleva 3 componentes:
# 1 - Una Etiqueta "Contador"
# 2 - Un lineEdit no editable, que muestre el valor de contador y que
# inicie con el número 88
# 3 - Un Botón "-"

import tkinter as tk

def decrementar():
    valor_actual = contador.get()
    contador.set(valor_actual - 1)

ventana = tk.Tk()
ventana.title("ContDecreciente")
ventana.geometry('200x100')
ventana.resizable(0,0)
ventana.config(bg='#0abfab')

marco = tk.Frame(ventana, bg='#52e5d5', padx=10, pady=10)
marco.pack(pady=25)

etiqueta = tk.Label(marco, text='Contador', bg='#52e5d5')
etiqueta.pack(side=tk.LEFT)

contador = tk.IntVar(value=88)

entrada = tk.Entry(marco, textvariable=contador, width=5, justify='center')
entrada.config(state='readonly')
entrada.pack(side=tk.LEFT, padx=15)

boton = tk.Button(marco, text='-', command=decrementar)
boton.pack(side=tk.LEFT)

ventana.mainloop()