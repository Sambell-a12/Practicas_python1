# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

print("Vas a ingresar un datos para un programa contable de inversiones")
inv = float(input("Ingresa una cantidad a invertir: "))
interes_anual = float(input("Ingrese el interes anual: "))
years = float(input("Ingrese el número de años: "))

Capital = (inv*(1+interes_anual)**years)

print("Este es el capital obetenidod e la inversión", Capital)
