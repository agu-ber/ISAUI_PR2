# Contar letras: Escribe una función que reciba una cadena y devuelva un diccionario
# con la frecuencia de cada letra en la cadena.

def contar_letras(cadena: str) -> dict:
    res = {}

    for letra in cadena:
        if letra != " ":
            if letra not in res.keys():
                res[letra] = 1
            else:
                res[letra] += 1

    res_ordenado = {clave: res[clave] for clave in sorted(res)}

    return res_ordenado

res = contar_letras("snkjasbajkfhkbadsjvbjscnkasjcbasfhauifabvuvebcfajdsbvnajkfaf")
for clave, valor in res.items():
    print(f"{clave}: {valor}")