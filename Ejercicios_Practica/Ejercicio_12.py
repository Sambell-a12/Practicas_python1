#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

bar_ant=int(input("Ingrese el numero de barras vendidadas que no son del día: "))

bar_pan_act=3.49
bar_pan_ant =bar_pan_act*0.6

print("El precio de la abra de pan es el siguiente: ",bar_pan_act)
print("El descuento por ser pan viejo de del 60% quedando del siguiente precio cada unidad: ",bar_pan_ant)
print(f"El precio normal {bar_pan_act*bar_ant}")
print(f"El precio final con descuento {bar_pan_ant*bar_ant}")
