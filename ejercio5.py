import os
os.system("clear")

isActive=True
while isActive:
    os.system("clear")
    print("bienvenido al generador de triangulos")
    try:
        n = int(input("ingrese la cantidad de la base del triangulo\npresione 0 si desea salir: "))
        if n == 0:
            isActive = False 
            print("gracias por usar el programa")
        elif n > 1:
            for i in range(1, n+1):
                print("*" * i)
                input("presione enter para continuar")
        else:
            print("no existe un triangulo con base 1")
            input("presione enter para continuar")
    except ValueError:
        print("debe ingresar un numero entero")
