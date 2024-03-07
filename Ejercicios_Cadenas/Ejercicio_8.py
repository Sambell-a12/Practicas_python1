#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio = input("Ingrese el precio de un producto en euros con dos decimales: ")

Euros = precio.split(".")

print(f"Euros: {Euros[0]}")
print(f"Centimos: {Euros[1]}")