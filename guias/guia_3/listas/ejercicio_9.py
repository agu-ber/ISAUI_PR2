# Producto de elementos: Escribe una función que tome una lista de números y
# devuelva el producto de todos los elementos.

def producto_lista(lista: list) -> int:
    res = 1

    for num in lista:
        res *= num

    return res

lista = [2, 5, 6, 7, 3, 4]
prod = producto_lista(lista)
print("El producto de todos los elementos es", prod)