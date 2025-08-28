import os
os.system("clear")
print("Tablas de multiplicacion")

numero=int(input("ingrese el numero para ver su tabla de multiplicacion: "))
print(f"\n tabla de multiplicar del {numero}")

for i in range(1,11):
    resultado=numero*i
    print(f"{numero} x {i} = {resultado}")