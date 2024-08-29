# Escribir una aplicación GUI (llamada Contador) como la que se ve en
# la figura. Con 3 botones (Count Up - Para incrementar, Count Down -
# Para restar y Reset - Para comenzar de cero). La aplicación lleva:
# 1 - Una etiqueta "Contador"
# 2 - Un lineEdit no editable, que muestre el contador y que inicie en 0
# 3 - 3 Botones

import tkinter as tk

def aumentar():
    valor_actual = contador.get()
    contador.set(valor_actual+1)

def disminuir():
    valor_actual = contador.get()
    contador.set(valor_actual-1)

def resetear():
    valor_actual = contador.get()
    contador.set(0)

ventana = tk.Tk()
ventana.title('Contador')
ventana.geometry('350x150')
ventana.resizable(0,0)
ventana.config(bg='#ff61cd')

marco = tk.LabelFrame(ventana, text='Contador', bg='#ff2fbd', fg='white', font=('Calibri', 12, 'bold'))
marco.pack(pady=40)

etiqueta = tk.Label(marco, text='Contador', bg='#ff2fbd', font=('Calibri', 12))
etiqueta.grid(row=0, column=0, padx=5)

contador = tk.IntVar(value=0)

entrada = tk.Entry(marco, textvariable=contador, width=5, state='readonly')
entrada.grid(row=0, column=1, padx=5)

boton_1 = tk.Button(marco, text='Count Up', command=aumentar, font=('Calibri', 10))
boton_1.grid(row=0, column=2, padx=5, pady=5)
boton_2 = tk.Button(marco, text='Count Down', command=disminuir, font=('Calibri', 10))
boton_2.grid(row=0, column=3, padx=5, pady=5)
boton_3 = tk.Button(marco, text='Reset', command=resetear, font=('Calibri', 10))
boton_3.grid(row=0, column=4, padx=5, pady=5)

ventana.mainloop()