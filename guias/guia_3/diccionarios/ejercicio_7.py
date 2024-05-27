# Sumar valores: Escribe una función que reciba un diccionario con valores numéricos y
# devuelva la suma de todos los valores.

def sumar_valores(diccionario: dict) -> int:
    res = 0

    for num in diccionario.values():
        res += num

    return res

diccionario = {
    1: 125,
    2: 324,
    3: 20,
    4: 452,
    5: 78
}
res = sumar_valores(diccionario)
print("La suma de los valores es", res)