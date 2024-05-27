# Agrupar por longitud: Escribe una función que reciba una lista de palabras y devuelva
# un diccionario donde las claves son las longitudes de las palabras y los valores son
# listas de palabras con esa longitud.

def agrupar_longitud(lista: list) -> dict:
    res = {}
    palabras = []
    palabras_sin_repetir = []
    longitudes = []

    for frase in lista:
        palabras += frase.split()

    for palabra in palabras:
        if palabra not in palabras_sin_repetir:
            palabras_sin_repetir.append(palabra)

    for palabra in palabras_sin_repetir:
        if len(palabra) not in longitudes:
            longitudes.append(len(palabra))
    longitudes.sort()

    for num in longitudes:
        lista_longitud = [palabra for palabra in palabras_sin_repetir if len(palabra) == num]
        res[num] = lista_longitud

    return res

lista = [
    "tengo que ir a comprar fruta",
    "me gusta el basquet",
    "ayer fui a comprar agua",
    "la fruta hace bien",
    "me tomé dos litros de agua en el partido de basquet"
]
res = agrupar_longitud(lista)
print(res)