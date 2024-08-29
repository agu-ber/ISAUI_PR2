# Escribir una aplicación GUI (llamada Películas). Su función será: al
# pulsar el botón Añadir, agregará en el listWidget el contenido de
# lineEdit (Películas).
# La aplicación lleva:
# 1 - 2 Etiquetas (Escribe el título de una película y Películas)
# 2 - Un lineEdit donde se escribirá el nombre de la película
# 3 - Un listWidget que registra las películas añadidas
# 4 - Un botón "Añadir"

import tkinter as tk
from tkinter import messagebox

def añadir():
    pelicula = entrada.get()

    # Verificar que no esté vacío y que no esté ya en la lista
    if pelicula and pelicula not in lista.get(0, tk.END):
        lista.insert(tk.END, pelicula)
        entrada.delete(0, tk.END)
    elif pelicula in lista.get(0, tk.END):
        messagebox.showwarning("Advertencia", "La película ya está en la lista.")

ventana = tk.Tk()
ventana.title('Películas')
ventana.geometry('400x340')
ventana.resizable(0,0)
ventana.config(bg='#3deadf')

marco = tk.LabelFrame(ventana, text='Lista de Películas', bg='#3db6ea', fg='white', font=('Calibri', 12, 'bold'))
marco.pack(pady=30)

etiqueta_1 = tk.Label(marco, text='Escribe el título de una película', bg='#3db6ea', font=('Calibri', 12))
etiqueta_1.grid(row=0, column=0, padx=5)
etiqueta_2 = tk.Label(marco, text='Películas', bg='#3db6ea', font=('Calibri', 12))
etiqueta_2.grid(row=0, column=1)

entrada = tk.Entry(marco)
entrada.grid(row=1, column=0)

lista = tk.Listbox(marco)
lista.grid(row=1,column=1, padx=15, pady=10)

boton = tk.Button(marco, text='Añadir', command=añadir)
boton.grid(row=2, column=1, pady=5)

ventana.mainloop()