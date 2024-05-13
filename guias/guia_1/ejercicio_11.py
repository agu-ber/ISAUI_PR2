# Crea un juego que le pida al usuario que piense un número entre 1 y 100. Luego, el 
# programa debe intentar adivinar ese número utilizando la estrategia de búsqueda 
# binaria. En cada intento, el programa debe preguntar al usuario si el número a 
# adivinar es mayor, menor o igual al número propuesto por el programa. El juego
# debe terminar cuando el programa adivine el número correcto.

msj_1 = "Bienvenido loko, necesito que pienses en un número " \
        "entre 1 y 100. Yo voy a adivinarlo con tu ayuda." \
        "\nMe vas a decir + si tu número es mayor, - si tu número " \
        "es menor o = si tu número es igual al mío."
print(msj_1)
input("Presiona Enter para iniciar...\n")

lim_inf = 1
lim_sup = 100
simbolo = ""
guess = 50

while simbolo != "=":

    simbolo = input(f"Mi número es {guess} ¿El tuyo es mayor, menor o igual? ")
    if simbolo == "+":
        lim_inf = guess
        guess = int((lim_inf + lim_sup) / 2)
    if simbolo == "-":
        lim_sup = guess
        guess = int((lim_inf + lim_sup) / 2)

print("\nGenial, lo adiviné! Gracias por jugar")