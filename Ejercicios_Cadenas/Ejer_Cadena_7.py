# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo = str(input("Inrgese su correo electronico: "))

nuevo_correo = correo[:correo.find('@')] + "@ceu.es"

print(nuevo_correo)