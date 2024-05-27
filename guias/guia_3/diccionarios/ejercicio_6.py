# Intercambiar valores: Crea una función que tome un diccionario y dos claves, e
# intercambie los valores de esas dos claves en el diccionario.

def intercambiar_claves(diccionario: dict, clave_1: str, clave_2: str) -> dict:
    res = diccionario.copy()

    for clave in res.keys():
        if clave == clave_1:
            res[clave] = diccionario[clave_2]
        elif clave == clave_2:
            res[clave] = diccionario[clave_1]

    return res

diccionario = {
    "001": "Agustín",
    "002": "Benjamín",
    "003": "Diego",
    "004": "Gastón"
}
clave_1 = "001"
clave_2 = "003"
dict_nuevo = intercambiar_claves(diccionario, clave_1, clave_2)
print(dict_nuevo)




