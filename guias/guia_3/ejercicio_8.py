# Concatenar listas: Escribe una función que reciba dos listas y devuelva una nueva lista
# que sea la concatenación de ambas.

def concat_listas(lista_1: list, lista_2: list) -> list:
    res = lista_1 + lista_2

    return res

lista_1 = [1, 2, 3]
lista_2 = [10, 20, 30]
lista_res = concat_listas(lista_1, lista_2)
print("La nueva lista es", lista_res)