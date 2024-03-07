#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

invertir = float(input("Ingrese la cantidad que quiere invertir: "))
interes_anual= float(input("Ingrese el interes anual"))
años = float(input("ingrese el número de años:"))

capital = ((invertir*(interes_anual/100+1))**años)


