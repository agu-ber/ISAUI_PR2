# Contar elementos: Escribe una función que reciba una lista y un valor, y devuelva
# cuántas veces aparece ese valor en la lista.

def contar_elemento(lista: list, valor: int) -> int:
    cont = 0

    for num in lista:
        if num == valor:
            cont +=1

    return cont

lista = [1, 2, 1, 3, 2, 1, 3, 1, 2, 3, 1]
valor = 1
res = contar_elemento(lista, valor)
print(f"El número {valor} aparece {res} veces")