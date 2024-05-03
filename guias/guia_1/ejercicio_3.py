# Escribe un programa en Python que solicite al usuario que ingrese la base y la
# altura de un triángulo, y luego calcule y muestre el área del triángulo.

msj_1 = "Calular Área de un Triángulo"

base = float(input("\nIngrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = (base * altura) / 2

area = round(area, 2) 

# Verifico si hay ceros innecesarios al final del valor y los elimino          
if str(area).endswith(".0"):
    area_str = str(area)     
    area_str = area_str[:-2]
    area = int(area_str)

msj_2 = f"\nEl área del triángulo es de {area}"
print(msj_2)