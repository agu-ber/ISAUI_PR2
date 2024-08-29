# Escribir una aplicación GUI (llamada Generador de números). Su
# función será: al pulsar el botón Generar, generará un número
# aleatorio en el rango de los dos Spin Box. La aplicación lleva:
# 1 - 3 Etiquetas (Número 1, Número 2 y Número Generado)
# 2 - 2 Spin Box
# 3 - 1 lineEdit que no pueda ser modificado
# 4 - 1 Botón "Generar"

import tkinter as tk
import random as rd
from tkinter import messagebox

def generar_numero():
    num_1 = int(spinbox_1.get())
    num_2 = int(spinbox_2.get())

    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    
    num_generado = rd.randint(num_1, num_2)
    numero.set(num_generado)

ventana = tk.Tk()
ventana.title('Generador de números')
ventana.geometry('350x200')
ventana.resizable(0,0)
ventana.config(bg='#da7b7b')

marco = tk.LabelFrame(ventana, text='Generador de números', bg='#cf3e3e', fg='white', font=('Calibri', 12, 'bold'))
marco.pack(pady=31)

etiqueta_1 = tk.Label(marco, text='Número 1', bg='#cf3e3e', font=('Calibri', 12))
etiqueta_1.grid(row=0, column=0, padx=5)
etiqueta_2 = tk.Label(marco, text='Número 2', bg='#cf3e3e', font=('Calibri', 12))
etiqueta_2.grid(row=1, column=0, padx=5)
etiqueta_3 = tk.Label(marco, text='Número Generado', bg='#cf3e3e', font=('Calibri', 12))
etiqueta_3.grid(row=2, column=0, padx=5)

spinbox_1 = tk.Spinbox(marco, from_=0, to=100, state='readonly')
spinbox_1.grid(row=0, column=1, padx=5)
spinbox_2 = tk.Spinbox(marco, from_=0, to=100, state='readonly')
spinbox_2.grid(row=1, column=1, padx=5)

numero = tk.IntVar(value=0)
entrada = tk.Entry(marco, textvariable=numero, state='readonly', width=22)
entrada.grid(row=2, column=1, padx=6)

boton = tk.Button(marco, text='Generar', command=generar_numero)
boton.grid(row=3, column=1, padx=5, pady=5)

ventana.mainloop()