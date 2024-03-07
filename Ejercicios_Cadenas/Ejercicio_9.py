# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha = input("Ingrese su necha de nacimiento con el sigiente formarto dd/mm/aaaa: ")

modi_fecha= fecha.split("/")

print(f"Día: {modi_fecha[0]}")
print(f"Mes: {modi_fecha[1]}")
print(f"Año: {modi_fecha[2]}")