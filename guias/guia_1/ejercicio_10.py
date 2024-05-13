# Crea un juego de ahorcado donde el jugador debe adivinar una 
# palabra oculta antes de que se agoten los intentos. 
# Puedes hacerlo con una lista predefinida de palabras.

import random

msj_1 = "Juego del ahorcado"
print(msj_1)

lista_palabras = [
    "python", "programacion", "algoritmo", "bucle", "condicional", "variable", "funcion",
    "clase", "objeto", "metodo", "cadena", "lista", "diccionario", "matriz", "recursividad",
    "depuracion", "compilador", "interprete", "github", "javascript", "servidor", "cliente",
    "backend", "frontend", "desarrollo", "deposito", "herencia", "polimorfismo", "encapsulamiento",
    "constante", "puntero", "estructura", "arreglo", "compilacion", "interpretacion", "archivo",
    "libreria", "framework", "interfaz", "conexion", "almacenamiento", "ciclo", "iteracion",
    "programador", "depurar", "optimizacion", "rendimiento", "portabilidad", "documentacion",
    "debugging", "analisis", "compilable", "inteligencia", "artificial", "base", "datos",
    "informacion", "consulta", "consulta", "red", "escalabilidad", "seguridad", "algoritmo",
    "ordenamiento", "busqueda", "grafos", "pila", "cola", "arbol", "listas", "ligadas",
    "concatenacion", "ejecucion", "interactivo", "sistema", "operativo", "evento", "asincrono"
]

palabra = random.choice(lista_palabras)
tablero = "_" * len(palabra)
errores = 0
print(tablero)

while tablero != palabra and errores != 6:
    letra = input("\nIngrese una letra: ")
    cont = 0

    for indice, caracter in enumerate(palabra):
        if caracter == letra:
            tablero = tablero[:indice] + letra + tablero[indice+1:]
            cont += 1
    print(tablero)

    if cont == 0:
        errores += 1
        print(f"{letra} no está. Te quedan {6-errores} intentos")

if tablero == palabra:
    print("\nFelicidades! Ganaste el juego")
elif errores == 6:
    print(f"\nPerdiste :( La palabra era {palabra}")