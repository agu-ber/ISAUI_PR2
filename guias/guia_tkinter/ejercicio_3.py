# Escribir una aplicación GUI (llamada Factorial) como la que se ve en
# la figura. Cada ves que se haga clic en el botón "Siguiente", debe
# calcular el factorial del primer lineEdit y mostrarlo en el segundo. Al
# dar siguiente (n se incrementa en 1) n = 2 con su factorial
# correspondiente. La aplicación lleva:
# 1 - Dos etiquetas: una para n y otra para Factorial (n)
# 2 - Dos lineEdit no editables
# 3 - Un botón siguiente

import tkinter as tk

def factorial():
    n_actual = n.get()
    n_siguiente = n_actual + 1
    n.set(n_siguiente)

    factorial = 1
    for i in range(1, n_siguiente+1):
        factorial *= i
    factorial_n.set(factorial)

ventana = tk.Tk()
ventana.title("Factorial")
ventana.geometry('350x120')
ventana.resizable(0,0)
ventana.config(bg="#26d300")

marco = tk.LabelFrame(ventana, text='Factorial', bg='#1ea600', fg='white', font=('Calibri', 12, 'bold'))
marco.pack(pady=29)

n = tk.IntVar(value=1)
factorial_n = tk.IntVar(value=1)

etiqueta_1 = tk.Label(marco, text='n', bg='#1ea600', font=('Calibri', 12))
etiqueta_1.grid(row=0, column=0, padx=5)
entrada_1 = tk.Entry(marco, textvariable=n, width=5, state='readonly')
entrada_1.grid(row=0, column=1, padx=5)

etiqueta_2 = tk.Label(marco, text='n!', bg='#1ea600', font=('Calibri', 12))
etiqueta_2.grid(row=0, column=2, padx=5)
entrada_2 = tk.Entry(marco, textvariable=factorial_n, width=20, state='readonly')
entrada_2.grid(row=0, column=3, padx=5)

boton = tk.Button(marco, text='Siguiente', command=factorial, font=('Calibri', 10))
boton.grid(row=0, column=4, padx=10, pady=5)

ventana.mainloop()