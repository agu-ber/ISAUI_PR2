# Elementos mayores que un valor: Escribe una función que tome una lista de números
# y un valor n, y devuelva una nueva lista con los elementos mayores que n.

def mayores_que(lista: list, n: int) -> list:
    res = []

    for num in lista:
        if num > n:
            res.append(num)

    return res

lista = [12, 56, 77, 30, 42, 59, 89, 3, 22, 99]
n = 50
lista_res = mayores_que(lista, n)
lista_res.sort()
print(f"Los números mayores a {n} son {lista_res}")