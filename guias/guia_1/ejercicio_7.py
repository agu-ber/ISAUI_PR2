# Desarrolla un juego en el que el programa selecciona aleatoriamente un número 
# entre 1 y 100 y el jugador debe adivinarlo. El programa debe proporcionar pistas al 
# jugador si el número ingresado es demasiado alto o demasiado bajo. El juego debe 
# continuar hasta que el jugador adivine correctamente el número.

import random

msj_1 = "Juego de Adivinar el Número" \
        "\nVoy a pensar un número del 1 al 100 y tenés que adivinarlo" \
        "\nNo te preocupes, te iré dando ayuda"
print(msj_1)

numero = random.randint(1, 100)
intento = 0
intentos = 0

while intento != numero:
    intento = int(input("\nIngresa un número: "))
    
    if intento > numero:
        print("Ingresaste un número mayor al que estoy pensando")
    elif intento < numero:
        print("Ingresaste un número menor al que estoy pensando")

    intentos += 1

msj_2 = f"¡Felicidades! Adivinaste el número en {intentos} intentos"
print(msj_2)