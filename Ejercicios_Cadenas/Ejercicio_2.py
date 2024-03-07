# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre=str(input("Ingrese su nombre completo: "))

minuscula = nombre.upper()
mayuscua = nombre.lower()
primer_mayos= nombre.title() #el title hace que cada caracter inicial de una cadena sea mayúscula y el resto minuscula


print(minuscula)
print(mayuscua)
print(primer_mayos)