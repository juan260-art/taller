import os
os.system("clear")

print("""bienvenido al programa de venta de productos
    1. registrarse
    2. iniciar secion
    3. salir""")


isActive=True

while isActive:
    os.system("clear")
    print(menulogin)
    option=int(input("seleccione una opcion"))   

match option:
    case 1:
        os.system("clear")
        print("registra tu usuario")
        user=input("ingrese su nombre de usuario")
        password=input("ingrese su contraseña")
    case 2:
        print("inicia secion")
        user=input("ingrese su nombre de usuario")
        password=input("ingrese su contraseña")
        userRegister=input("ingrese su nombre de usuario: ")
        os.system("clear")
        passwordregister=input("ingrese su contraseña: ")
        os.system("clear")

      