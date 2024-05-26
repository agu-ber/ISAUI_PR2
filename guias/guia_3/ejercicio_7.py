# Invertir lista: Escribe una función que tome una lista y devuelva una nueva lista
# con los elementos en orden inverso.

def invertir_lista(lista: list) -> list:
    res = []
    can = len(lista)

    for i in range(can-1, -1, -1):
        ele = lista[i]
        res.append(ele)

    return res

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_res = invertir_lista(lista)
print("La lista invertida es", lista_res)