import re
tarjeta=input("Ingrese el número de su tarjeta: ")
x=re.findall(r"[4-6]{1}[0123789]{3}\d{3}\d{1}\d{3}\d{1}\d{3}\d{1}|[4-6]{1}[0123789]{3}-\d{3}\d{1}-\d{3}\d{1}-\d{3}\d{1}",tarjeta)
if x:
    print(f"{tarjeta} -> Valid")
else:
    print(f"{tarjeta} -> Invalid")
# Los números de tarjetas deben iniciar con 4, 5 o 6
#La cantidad de dígitos deben ser 16
#Deben ser digitos entre [0 - 9]
#Puede tener dígitos en grupos de 4, separados por un guión "-".
#No debe contener ningún otro separador como ' ' , '_', etc.
#No debe tener 4 o más dígitos repetidos consecutivos.