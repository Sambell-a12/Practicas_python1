#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nom = str(input("Ingrese su nombre: "))
num1 = int(input("Ingrese la cantidad de veces que quiere imprimir el nombre: "))

for i in range(num1):
    print(f"Hola que tal {nom}")
    