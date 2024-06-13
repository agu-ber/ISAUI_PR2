# Palabras por letra inicial : Escribe una función que tome una lista de palabras 
# y devuelva un diccionario donde las claves son las letras iniciales de las palabras 
# y los valores son listas de palabras que comienzan con esa letra.

def letra_inicial(lista: list) -> dict:
    res = {}
    iniciales = []
    
    for palabra in lista:
        inicial = palabra[0]

        if inicial not in iniciales:
            iniciales.append(inicial)

    iniciales.sort()
    for letra in iniciales:
        lista_palabras = [palabra for palabra in lista if palabra[0] == letra]
        res[letra] = lista_palabras

    return res    


lista = [
    "python", "programacion", "algoritmo", "bucle", "condicional", "variable", "funcion",
    "clase", "objeto", "metodo", "cadena", "lista", "diccionario", "matriz", "recursividad",
    "depuracion", "compilador", "interprete", "github", "javascript", "servidor", "cliente",
    "backend", "frontend", "desarrollo", "deposito", "herencia", "polimorfismo", "encapsulamiento",
    "constante", "puntero", "estructura", "arreglo", "compilacion", "interpretacion", "archivo",
    "libreria", "framework", "interfaz", "conexion", "almacenamiento", "ciclo", "iteracion",
    "programador", "depurar", "optimizacion", "rendimiento", "portabilidad", "documentacion",
    "debugging", "analisis", "compilable", "inteligencia", "artificial", "base", "datos",
    "informacion", "consulta", "consulta", "red", "escalabilidad", "seguridad", "algoritmo",
    "ordenamiento", "busqueda", "grafos", "pila", "cola", "arbol", "listas", "ligadas",
    "concatenacion", "ejecucion", "interactivo", "sistema", "operativo", "evento", "asincrono"
]    

res = letra_inicial(lista)
print(res)