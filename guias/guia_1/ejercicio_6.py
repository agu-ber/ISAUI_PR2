# Escribe un programa en Python que valide una contraseña ingresada por 
# el usuario. La contraseña debe cumplir con los siguientes requisitos:
# · Debe tener al menos 8 caracteres de longitud.
# · Debe contener al menos una letra mayúscula, una letra minúscula, un 
# número y un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
# El programa debe informar al usuario si la contraseña es válida o no.

msj_1 = "Validación de contraseña" \
        "\n\nLa contraseña debe cumplir estos requisitos:" \
        "\n· Debe tener al menos 8 caracteres de longitud." \
        "\n· Debe contener al menos una letra mayúscula, una letra minúscula, un" \
        "\nnúmero y un carácter especial (por ejemplo, !, @, #, $, %, etc.)."
print(msj_1)

contraseña = input("\nIngrese su contraseña: ")

longitud = False
mayuscula = False
minuscula = False
numero = False
caracter_especial = False

if len(contraseña) >= 8:
    longitud = True
for i in contraseña:
    if i in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ": # También podría usarse i.isupper()
        mayuscula = True
    elif i in "abcdefghijklmnñopqrstuvwxyz": # i.islower()
        minuscula = True
    elif i in "0123456789": # i.isdigit()
        numero = True
    elif i in "!@#$%^&*()_+-=[]}{|;:,.<>?`~":
        caracter_especial = True

if longitud and mayuscula and minuscula and numero and caracter_especial:
    print("¡La contraseña es válida!")
else:
    print("La contraseña no es válida. Inténtelo nuevamente")