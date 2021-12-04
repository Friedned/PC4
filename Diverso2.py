x=input("Elige un número del 1 al 10: ")
import os
try:
    with open(f"tabla{x}.txt","r") as fichero:
        for linea in fichero:
            print(linea)
except:
    print("El fichero no existe")