# Escribir una aplicación GUI (llamada Calculadora) que funcione como
# una simple calculadora. La aplicación lleva:
# 1 - Tres etiquetas (Primer número, Segundo número y Resultado)
# 2 - 3 lineEdit (el lineEdit de Resultado no se puede modificar)
# 3 - 6 Botones (+, -, *, /, % y RESET). El botón CLEAR debe borrar los
# 3 lineEdit. Al presionar (+, -, *, / o %) el único campo que se modifica
# es Resultado.

import tkinter as tk

def calcular(operacion):
    num_1 = float(entrada_1.get())
    num_2 = float(entrada_2.get())

    if operacion == '+':
        resultado.set(num_1 + num_2)
    elif operacion == '-':
        resultado.set(num_1 - num_2)
    elif operacion == '*':
        resultado.set(num_1 * num_2)
    elif operacion == '/':
        if num_2 != 0:
            resultado.set(num_1 / num_2)
        else:
            resultado.set('ERROR')
    elif operacion == '%':
        resultado.set(num_1 % num_2)

def resetear():
    entrada_1.delete(0, tk.END)
    entrada_2.delete(0, tk.END)
    resultado.set('')

def validar_entrada(texto):
    # Permitir solo números y el punto decimal
    return texto == "" or texto.isdigit() or (texto.replace('.', '', 1).isdigit() and texto.count('.') < 2)

ventana = tk.Tk()
ventana.title('Calculadora')
ventana.geometry('280x250')
ventana.resizable(0,0)
ventana.config(bg='#fbdf63')

marco = tk.LabelFrame(ventana, text='Calculadora', bg='#ffd000', fg='white', font=('Calibri', 12, 'bold'))
marco.pack(pady=30)

# Crear validación para las entradas
validacion = ventana.register(validar_entrada)

etiqueta_1 = tk.Label(marco, text='Primer número', bg='#ffd000')
etiqueta_1.grid(row=0, column=0)
etiqueta_2 = tk.Label(marco, text='Segundo número', bg='#ffd000')
etiqueta_2.grid(row=1, column=0)
etiqueta_3 = tk.Label(marco, text='Resultado', bg='#ffd000')
etiqueta_3.grid(row=2, column=0)

entrada_1 = tk.Entry(marco, validate="key", validatecommand=(validacion, '%P'))
entrada_1.grid(row=0, column=1, padx=5)
entrada_2 = tk.Entry(marco, validate="key", validatecommand=(validacion, '%P'))
entrada_2.grid(row=1, column=1, padx=5)

resultado = tk.StringVar()
entrada_3 = tk.Entry(marco, textvariable=resultado, state='readonly')
entrada_3.grid(row=2, column=1)

boton_1 = tk.Button(marco, text='+', command=lambda: calcular('+'), width=5)
boton_1.grid(row=3, column=0, pady=2)
boton_2 = tk.Button(marco, text='-', command=lambda: calcular('-'), width=5)
boton_2.grid(row=3, column=1, pady=2)
boton_3 = tk.Button(marco, text='*', command=lambda: calcular('*'), width=5)
boton_3.grid(row=4, column=0, pady=2)
boton_4 = tk.Button(marco, text='/', command=lambda: calcular('/'), width=5)
boton_4.grid(row=4, column=1, pady=2)
boton_5 = tk.Button(marco, text='%', command=lambda: calcular('%'), width=5)
boton_5.grid(row=5, column=0, pady=2)
boton_6 = tk.Button(marco, text='CLEAR', command=resetear, width=5)
boton_6.grid(row=5, column=1, pady=2)

ventana.mainloop()