import os
os.system("clear")
print("numero mayor")

primernumero=int(input("ingresa el primer numero: "))
segundonumero=int(input("ingrese el segundo numero: "))
tercernumero=int(input("ingrese el tercer numero: "))

if primernumero>segundonumero and tercernumero:
    print("el numero mayor:",primernumero)

if segundonumero>primernumero and tercernumero:
    print("el numero mayor es:",segundonumero)

if tercernumero>primernumero and segundonumero:
    print("el numero mayor es:",primernumero) 