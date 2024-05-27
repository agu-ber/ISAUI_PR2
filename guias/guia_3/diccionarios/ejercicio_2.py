# Diccionario inverso: Escribe una función que tome un diccionario y devuelva uno
# nuevo que invierta las claves y los valores.

def dict_inverso(diccionario: dict) -> dict:
    res = {}

    for clave, valor in diccionario.items():
        res[valor] = clave

    return res

diccionario = {
    "carlos": 12,
    "jorge": 9,
    "pedro": 11,
    "juan": 7,
    "luciano": 9
}
res = dict_inverso(diccionario)
print(res)