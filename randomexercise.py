import os 
import random

x = random.randint(1, 10)
print(x)

isActive=True
while isActive:
    os.system("clear")
    print("bienvenido al minijuego de adivinar un numero entre 1, 10")

numero = int(input("ingrese el numero que cree que es el numero aleatorio: "))

if numero == x:
        print("\nFelicidaces, adivinaste el numero")
        input("presiona enter para iniciar")
        isActive=False
else:
        print(f"\nlo siento, el numero era: {x}")
        input("presiona enter para continuar")
        