# Promedio de una lista: Crea una función que calcule el promedio de los números en
# una lista dada.

def promedio(lista: list) -> float:

    suma = sum(lista)
    res = suma / len(lista)

    return res

lista = [2.6, 2.9, 1.2, 3.4, 1.7, 4.5, 3.1]
prom = promedio(lista)
prom_round = round(prom, 4)
print("El promedio es", prom_round)