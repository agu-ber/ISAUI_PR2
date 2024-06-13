# Notas de estudiantes : Escribe una función que recibe un diccionario donde
# las claves son nombres de estudiantes y los valores son listas de sus calificaciones. 
# La función debe devolver un nuevo diccionario con las mismas claves 
# pero donde los valores son la calificación promedio de cada estudiante.

def notas_estudiantes(diccionario: dict) -> dict:
    res = {}

    for clave, valor in diccionario.items():
        promedio = 0
        for notas in valor:
            promedio = sum(valor) / len(valor)
            res[clave] = round(promedio, 2)
    
    return res

diccionario = {
    "Bernasconi": [8, 7, 6],
    "Briolini": [10, 5, 7],
    "Garnica": [1, 2, 5],
    "Luna": [9, 9, 10]
}
res = notas_estudiantes(diccionario)
print(res)