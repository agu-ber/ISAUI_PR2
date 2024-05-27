# Diccionario de listas: Escribe una función que tome un diccionario donde los valores
# son listas y devuelva una lista que contenga todos los elementos de las listas del
# diccionario.

def dict_listas(diccionario: dict) -> list:
    res = []

    for clave, valor in diccionario.items():
        res += valor

    return res

diccionario = {
    "clubes": ["Boca", "River", "Belgrano"],
    "países": ["Argentina", "Brasil", "Bolivia"],
    "nombres": ["Juan", "Pedro", "Pablo"]
}
res = dict_listas(diccionario)
print(res)