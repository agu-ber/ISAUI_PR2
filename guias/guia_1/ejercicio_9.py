# Desarrolla una calculadora que calcule el factorial de un número ingresado por el 
# usuario. El factorial de un número entero positivo n se define como el producto de
# todos los enteros positivos menores o iguales a n. El programa debe manejar 
# números enteros grandes y mostrar el resultado.

msj_1 = "Calculadora de Factorial"
print(msj_1)

n = int(input("\nIngresa el número a calcular: "))
factorial = 1

for i in range(1, n+1):
    factorial *= i

msj_2 = f"El factorial de {n} es {factorial}"
print(msj_2)