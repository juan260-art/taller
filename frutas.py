import os

os.system ("clear")

frutas=input("de que fruta desea saber el precio")

match frutas:
    case "manzana":
        print("la manzana vale 2000")
    case "pera":
        print("la pera vale 3000")
    case "mango":
        print("el mango vale 2300")
    case _:
        print("ingrese una fruta valida")
        
