# Contar palabras en frases: Escribe una función que reciba una lista de frases y
# devuelva un diccionario donde las claves son las palabras y los valores son las
# frecuencias de esas palabras en todas las frases.

def contar_palabras(lista: list) -> dict:
    res = {}
    palabras = []

    for frase in lista:
        palabras += frase.split()

    for palabra in palabras:
        if palabra not in res.keys():
            res[palabra] = 1
        else:
            res[palabra] += 1

    # El parámetro key de la función sorted permite aplicar una función al elemento
    # comparado antes de que se realice la comparación. Aplico una función lambda que
    # busca el elemento de índice 1 en la tupla clave valor correspondiente a cada item
    res_ordenado = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))

    return res_ordenado

lista = [
    "tengo que ir a comprar fruta",
    "me gusta el basquet",
    "ayer fui a comprar agua",
    "la fruta hace bien",
    "me tomé dos litros de agua en el partido de basquet"
]
res = contar_palabras(lista)
print(res)