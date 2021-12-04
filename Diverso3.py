n=input("Ingrese numero de fichero que desea abrir (entre 1 y 10): ")
m=int(input("Ingrese la linea que desea mostrar (entre 1 y 10): "))
try:
    with open(f"tabla{n}.txt","r") as fichero:
        linea=fichero.readlines()[m]
    print(linea)
except:
    print("El fichero no existe")