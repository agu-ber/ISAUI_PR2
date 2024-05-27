# Actualizar diccionario: Escribe una función que tome un diccionario y una lista de
# tuplas (clave, valor) y actualice el diccionario con esas tuplas.

def actualizar_dict(diccionario: dict, lista: list) -> dict:

    for clave, valor in lista:
        diccionario[clave] = valor

    return diccionario

diccionario = {
    "Brasil": 5,
    "Alemania": 4,
    "Italia": 4
}
lista = [
    ("Argentina", 3),
    ("Francia", 2),
    ("Uruguay", 2)
]
res = actualizar_dict(diccionario, lista)
print(res)
