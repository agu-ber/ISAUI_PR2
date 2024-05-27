# Filtrar diccionario: Escribe una función que reciba un diccionario y una lista de claves,
# y devuelva un nuevo diccionario solo con las claves especificadas.

def filtrar_dict(diccionario: dict, lista: list) -> dict:
    res = {}

    for clave in lista:
        if clave in diccionario.keys():
            res[clave] = diccionario[clave]

    return res

diccionario = {
    "001": "Agustín",
    "002": "Federico",
    "003": "Damián",
    "004": "Matías",
    "005": "Bautista" 
}
lista = ["002", "004"]
dict_nuevo = filtrar_dict(diccionario, lista)
print(dict_nuevo)