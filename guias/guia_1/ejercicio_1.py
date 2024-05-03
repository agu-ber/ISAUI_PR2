# Escribe un programa en Python que solicite al usuario que ingrese 
# tres números y luego calcule y muestre el promedio de esos números.

msj_1 = "Calculadora de Promedio"
print(msj_1)

num_1 = int(input("\nIngrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Ingrese el tercer número: "))
prom = (num_1 + num_2 + num_3) / 3

if prom.is_integer():
    prom = int(prom)

msj_2 = f"\nEl promedio de {num_1}, {num_2} y {num_3} es {prom}"
print(msj_2)