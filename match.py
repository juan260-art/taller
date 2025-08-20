opcion = int(input("elige una opcion (1-3): "))

match opcion: 
    case 1:
        print("has elegido la opcion 1")
    case 2:
        print("has elegido la opcion 2")
    case 3:
        print("has elegido la opcion 3")
    case _:
        print("opcion no valida")
