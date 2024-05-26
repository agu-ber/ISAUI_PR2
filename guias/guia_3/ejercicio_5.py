# Eliminar duplicados: Crea una función que tome una lista y devuelva una nueva lista
# sin elementos duplicados.

def eliminar_duplicados(lista: list) -> list:
    res = []

    for num in lista:
        if num not in res:
            res.append(num)

    return res

lista = [1, 2, 1, 3, 2, 1, 3, 1, 2, 3, 1]
lista_res = eliminar_duplicados(lista)
lista_res.sort()
print("La lista sin duplicados es", lista_res)

