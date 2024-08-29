# Escribir una aplicación GUI (llamada ContCreciente) como la que se
# ve en la figura. Cada vez que se haga clic en el botón "+", el valor del
# contador se incrementa en 1. El programa lleva 3 componentes:
# 1 - Una Etiqueta "Contador"
# 2 - Un lineEdit no editable, que muestre el valor del contador
# 3 - Un Botón "+"

import tkinter as tk

def incrementar():
    valor = contador.get() # Obtener el valor actual del contador
    contador.set(valor + 1)

ventana = tk.Tk()
ventana.title("ContCreciente")
ventana.geometry('200x25')
ventana.config(bg='white')
ventana.resizable(0,0)

# Crear una variable StringVar para manejar el valor del contador
contador = tk.IntVar(value=0)

etiqueta = tk.Label(ventana, text="Contador")
etiqueta.grid(row=0, column=0)

# LineEdit no editable que muestra el valor del contador
entrada = tk.Entry(ventana, textvariable=contador, state="readonly")
entrada.grid(row=0, column=1)

boton = tk.Button(ventana, text="+", command=incrementar)
boton.grid(row=0, column=2)

ventana.mainloop()