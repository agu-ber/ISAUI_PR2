# Encontrar índice: Escribe una función que reciba una lista y un valor, y devuelva el
# índice de la primera aparición de ese valor en la lista, o -1 si el valor no está presente.

def encontrar_indice(lista: list, valor: int) -> int:
    res = -1

    for num in lista:
        if num == valor:
            res = lista.index(num)
            break

    return res

lista = [2, 3, 4, 6, 5, 4, 1, 2, 3, 1, 4, 5]
valor = 1
indice = encontrar_indice(lista, valor)
print(f"El valor {valor} tiene el índice {indice}")