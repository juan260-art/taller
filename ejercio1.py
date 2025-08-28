import os
os.system("clear")

print("\nconversor de monedas")
print("seleccione una opcion: ")
print("1.COP-->USD")
print("2.USD-->JPY")
print("3.JPY-->COP")

opcion=input("opcion: ")

copusd=0.00025
usdjpy=147.0
jpycop=28.0

signos={"COP": "$",
          "USD": "US$",
          "JPY": "Y"}

if opcion=="1":
    cantidad=float(input("ingrese la cantidad en COP que desea convertir a USD: "))
    resultado=cantidad*copusd
    print(f"\n {signos['COP']} {cantidad} COP ={signos['USD']}{round(resultado,2)}")
    
elif opcion=="2":
    cantidad=float(input("ingrese la cantidad en USD que desea convertir a JPY: "))
    resultado=cantidad*usdjpy
    print(f"\n {signos['USD']}{cantidad} USD ={signos['JPY']}{round(resultado,2)}")
    
elif opcion=="3":
    cantidad=float(input("ingrese la cantidad de JPY que desea convertir a COP:  ")) 
    resultado=cantidad*jpycop
    print(f"\n {signos['JPY']}{cantidad} Y ={signos['COP']}{round(resultado,2)}")   
    
else:
    print(" X opcion no valida, intentelo de nuevo X ")