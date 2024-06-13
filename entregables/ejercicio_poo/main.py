# Se importan las clases Electronico y Alimento
from electronico import Electronico
from alimento import Alimento

# Se crean instancias de las clases
e = Electronico("Smartphone", 800000, 15, "Samsung", "Galaxy A53")
a = Alimento("Leche entera", 1500, 65, "18/08/2024")

# Se muestra la información de los productos
print(e.mostrar_info())
print(a.mostrar_info())