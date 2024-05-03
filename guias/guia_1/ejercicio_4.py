# Desarrolla un programa en Python que solicite al usuario que ingrese una frase
# y luego cuente y muestre el número de palabras en esa frase.


msj_1 = "Contador de Palabras"
print(msj_1)

frase = input("\nIngrese una frase: ")

'''
contador = 1
for i in frase:
    if i == " ":
        contador += 1
'''

palabras = frase.split()
cant_palabras = len(palabras)

msj_2 = f"\nSu frase contiene {cant_palabras} palabras"
print(msj_2)