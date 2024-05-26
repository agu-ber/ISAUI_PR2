# Máximo y mínimo: Escribe una función que reciba una lista de números y devuelva el
# valor máximo y el mínimo de la lista.

def min_max(lista: list) -> int:
    
    lista.sort()
    minimo = lista[0]
    maximo = lista[len(lista)-1]

    return minimo, maximo

lista = [143, 122, 56, 202, 31, 203, 89, 101]
min, max = min_max(lista)
print(f"El mínimo es {min} y el máximo es {max}")