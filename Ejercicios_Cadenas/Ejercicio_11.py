# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

nom = input("Ingrese el nombre de un producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingresar la cantidad del producto: "))
total = cantidad*precio

print(f"{nom}: {cantidad} unidades x {precio:9.3f} = {total:11.2f}")

#eso esta raro 