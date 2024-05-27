# Valores únicos: Escribe una función que reciba un diccionario y devuelva una lista de
# valores únicos en el diccionario.

def valores_unicos(diccionario: dict) -> dict:
    res = []

    for valor in diccionario.values():
        if valor not in res:
            res.append(valor)

    return res

diccionario = {
    1: "Córdoba",
    2: "Buenos Aires",
    3: "Córdoba",
    4: "Mendoza",
    5: "Santa Fe",
    6: "Córdoba",
    7: "Buenos Aires"
}
lista = valores_unicos(diccionario)
print(lista)