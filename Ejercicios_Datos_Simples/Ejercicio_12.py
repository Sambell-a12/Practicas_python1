# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

pan = 3.49
Descuento = 0.60

venta = int(input("Ingrese la cantidad de barras vendidas: "))

print(f"El precio normal de un pan freco es de {pan}")

print("El descuento que se la hara por no ser fresco es de 60%")

Total = ((venta*pan)*Descuento)

print(f"Total de la compra con descuento = {Total}")