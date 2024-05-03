# Desarrolla un programa en Python que convierta una cantidad de dinero de dólares
# estadounidenses a euros. El programa debe solicitar al usuario que ingrese la
# cantidad en dólares y luego mostrar la cantidad equivalente en euros, utilizando un
# tipo de cambio fijo.

msj_1 = "Conversor de Moneda"
print(msj_1)

dol = float(input("\nIngrese la cantidad de dólares estadounidenses a convertir: "))
eur = dol * 0.93

dol = round(dol, 2)
eur = round(eur, 2)

# Se verifica si los valores tienen ceros innecesarios y se los elimina
if str(dol).endswith(".0"):
    dol_str = str(dol)
    dol_str = dol_str[:-2] 
    dol = int(dol_str)    

if str(eur).endswith(".0"):
    eur_str = str(eur)
    eur_str = eur_str[:-2]
    eur = int(eur_str)    

msj_2 = f"\nAl 2 de Mayo de 2024, {dol} dólares estadounidenses equivalen a {eur} euros"
print(msj_2)