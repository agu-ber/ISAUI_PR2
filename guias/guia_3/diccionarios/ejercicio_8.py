# Diccionario de frecuencias: Escribe una función que reciba una lista de palabras y
# devuelva un diccionario con la frecuencia de cada palabra.

def frecuencias(lista: list) -> dict:
    diccionario = {}

    for palabra in lista:
        if palabra not in diccionario.keys():
            diccionario[palabra] = 1
        else:
            diccionario[palabra] += 1

    return diccionario

lista = [
    "Boca",
    "River",
    "River",
    "Racing",
    "Boca",
    "Boca"
]
res = frecuencias(lista)
print(res)