# Suma de elementos: Escribe una función que tome una lista de números y devuelva la
# suma de todos los elementos en la lista.

def suma_lista(lista: list) -> int:

    res = sum(lista)

    return res

lista = [1, 2, 3, 4, 5, 6, 7, 8]
suma = suma_lista(lista)
print("La suma es", suma)