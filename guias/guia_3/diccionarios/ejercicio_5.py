# Diccionario de cuadrados: Escribe una función que reciba un número n y devuelva un
# diccionario con los números de 1 a n como claves y sus cuadrados como valores.

def dict_cuadrados(n: int) -> dict:
    res = {}

    for num in range(1, n+1):
        cuadrado = num ** 2
        res[num] = cuadrado

    return res

diccionario = dict_cuadrados(15)
print(diccionario)