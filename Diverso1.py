import os
numero=int(input("Ingrese un número del 1 al 10: "))
with open(f'tabla{numero}.txt','w') as f:
    for i in range(1,13):
        multiplicacion=i*numero
        escribir=f"{numero} x {i} = {multiplicacion} \n"
        f.write(escribir)