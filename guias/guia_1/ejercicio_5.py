# Mejora el programa de conversión de temperatura que escribiste anteriormente
# para que permita al usuario elegir entre convertir de grados Celsius a grados
# Fahrenheit o viceversa.

msj_1 = "Conversor de Temperatura"
print(msj_1)

tipo_grado = input("\nIngrese C para usar grados Celsius o F para Fahrenheit: ")

if tipo_grado in ["C", "c"]:
    celsius = float(input("\nIngrese grados Celsius: "))
    res = (celsius * 9/5) + 32
    str_grado = "Fahrenheit"
elif tipo_grado in ["F", "f"]:
    fahrenheit = float(input("\nIngrese grados Fahrenheit: "))
    res = (fahrenheit-32) * 5/9
    str_grado = "Celsius"
else:
    print("\nNo ha ingresado una opción válida")
    raise SystemExit # Se detiene el programa para que no se ejecute el resto del código

res = round(res, 1)

if str(res).endswith(".0"):
    str_res = str(res)
    str_res = str_res[:-2]
    res =  int(str_res)

msj_2 = f"Equivale a {res} grados {str_grado}"
print(msj_2)