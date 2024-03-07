# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

Productos = input("Ingrese la lista de compras separando los prodcutos con una ',' : ")

modi = Productos.count(",")
canasta = Productos.split(",")

for i in range(modi+1):
    print(canasta[i])
