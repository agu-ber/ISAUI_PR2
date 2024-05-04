# Escribe un programa en Python que genere una contraseña aleatoria para el usuario.
# La contraseña debe tener una longitud de al menos 12 caracteres y debe contener
# una combinación de letras (mayúsculas y minúsculas), números y caracteres especiales.
# El programa debe mostrar la contraseña generada al usuario.

import random

msj_1 = "Generador de contraseña"
print(msj_1)
input("Presiona Enter para continuar ")

mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
caracteres_especiales = "!@#$%^&*()_+-=[]}{|;:,.<>?`~"
caracteres = [] # Guardo los caracteres en una lista para luego convertirlo en una cadena

# Me aseguro de que tenga al menos 3 caracteres de cada tipo, recordemos que el mínimo es 12
for _ in range(3):
    caracteres.append(random.choice(mayusculas))
    caracteres.append(random.choice(minusculas))
    caracteres.append(random.choice(numeros))
    caracteres.append(random.choice(caracteres_especiales))   

# Defino una longitud restante aleatoria, primero le resto 12 a ambos extremos ya que ya tengo
# 12 caracteres generados. Decidí una longitud máxima de 30 caracteres.
longitud_restante = random.randint(0, 18) 
    
# Agrego caracteres aleatorios para completar la contraseña
for _ in range(longitud_restante):
    caracteres.append(random.choice(mayusculas + minusculas + numeros + caracteres_especiales))    

random.shuffle(caracteres) # Mezclo la contraseña
contraseña = "".join(caracteres) # Genero una string uniendo todos los caracteres generados

msj_2 = f"\nTu contraseña es de {longitud_restante + 12} caracteres y es {contraseña}"
print(msj_2)