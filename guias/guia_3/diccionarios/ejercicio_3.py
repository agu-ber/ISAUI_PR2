# Merge de diccionarios: Crea una función que tome dos diccionarios y devuelva uno
# nuevo que combine ambos (en caso de conflicto, usa los valores del segundo
# diccionario).

def dict_merge(dict_1: dict, dict_2: dict) -> dict:
    dict_nuevo = dict_1.copy()
    
    for clave, valor in dict_2.items():
        dict_nuevo[clave] = valor 
    
    return dict_nuevo

dict_1 = {
    "benjamin": 23,
    "agustin": 22,
    "diego": 19
}
dict_2 = {
    "gaston": 3,
    "diego": 2,
    "mateo": 4,
    "julian": 5
}

res = dict_merge(dict_1, dict_2)
print(res)