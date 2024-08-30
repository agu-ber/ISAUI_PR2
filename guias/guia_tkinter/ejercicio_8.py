# Escribir una aplicación GUI (llamada Calculadora 2) como la que se ve
# en la figura y que funcione como una calculadora. La aplicación lleva:
# 1 - 4 Etiquetas (Valor 1, Valor 2, Resultado y Operaciones)
# 2 - 4 radioButton (Sumar, Restar, Multiplicar y Dividir)
# 3 - 3 lineEdit (el lineEdit Resultado no puede ser modificado)
# 4 - 1 botón Calcular, que al ser presionado realice la operación
# correspondiente.

import tkinter as tk
from tkinter import messagebox

def calcular():
    num_1 = entrada_1.get()
    num_2 = entrada_2.get()
    operacion = opcion_elegida.get()

    # Validar que los valores de entrada no estén en blanco
    if not num_1 or not num_2:
        messagebox.showwarning("Advertencia", "Por favor, ingrese ambos valores.")
        return

    # Validar que se haya elegido una operación
    if operacion == 0:
        messagebox.showwarning("Advertencia", "Por favor, seleccione una operación.")
        return

    num_1 = float(num_1)
    num_2 = float(num_2)
    res = 0

    if operacion == 1:
        res = num_1 + num_2
    elif operacion == 2:
        res = num_1 - num_2
    elif operacion == 3:
        res = num_1 * num_2
    elif operacion == 4:
        if num_2 != 0:    
            res = num_1 / num_2
        else:
            res = "ERROR"

    resultado.set(res)

def validar_entrada(texto):
    # Permitir solo números y el punto decimal
    return texto == "" or texto.isdigit() or (texto.replace('.', '', 1).isdigit() and texto.count('.') < 2)

ventana = tk.Tk()
ventana.title('Calculadora 2')
ventana.geometry('400x250')
ventana.resizable(0,0)
ventana.config(bg='#8ef3ff')

marco = marco = tk.LabelFrame(ventana, text='Caluladora', bg='#2de9ff', fg='grey', font=('Calibri', 12, 'bold'))
marco.pack(pady=30)

etiqueta_1 = tk.Label(marco, text='Valor 1', bg='#2de9ff', font=('Calibri', 12))
etiqueta_1.grid(row=1, column=0, padx=5)
etiqueta_2 = tk.Label(marco, text='Valor 2', bg='#2de9ff', font=('Calibri', 12))
etiqueta_2.grid(row=2, column=0, padx=5)
etiqueta_3 = tk.Label(marco, text='Resultado', bg='#2de9ff', font=('Calibri', 12))
etiqueta_3.grid(row=3, column=0, padx=5)
etiqueta_4 = tk.Label(marco, text='Operaciones', bg='#2de9ff', font=('Calibri', 12))
etiqueta_4.grid(row=0, column=2, padx=5)

# Crear validación para las entradas
validacion = ventana.register(validar_entrada)

entrada_1 = tk.Entry(marco, validate="key", validatecommand=(validacion, '%P'))
entrada_1.grid(row=1, column=1)
entrada_2 = tk.Entry(marco, validate="key", validatecommand=(validacion, '%P'))
entrada_2.grid(row=2, column=1)

resultado = tk.StringVar()
entrada_3 = tk.Entry(marco, textvariable=resultado, state='readonly')
entrada_3.grid(row=3, column=1)

# Crear un Frame para los RadioButtons
marco_radiobuttons = tk.Frame(marco, bg='#2de9ff')
marco_radiobuttons.grid(row=1, column=2, rowspan=4, padx=15)

opcion_elegida = tk.IntVar(value=0)
opcion_1 = tk.Radiobutton(marco_radiobuttons, text='Sumar', variable=opcion_elegida, value=1, bg='#2de9ff')
opcion_1.pack(anchor='w')
opcion_2 = tk.Radiobutton(marco_radiobuttons, text='Restar', variable=opcion_elegida, value=2, bg='#2de9ff')
opcion_2.pack(anchor='w')
opcion_3 = tk.Radiobutton(marco_radiobuttons, text='Multiplicar', variable=opcion_elegida, value=3, bg='#2de9ff')
opcion_3.pack(anchor='w')
opcion_4 = tk.Radiobutton(marco_radiobuttons, text='Dividir', variable=opcion_elegida, value=4, bg='#2de9ff')
opcion_4.pack(anchor='w')

boton = tk.Button(marco, text='Calcular', command=calcular, bg='#8ef3ff')
boton.grid(row=5, column=2, pady=10)

ventana.mainloop()