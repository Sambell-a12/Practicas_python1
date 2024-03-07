# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

print("Vas a ingresar numeros para obtener el cociente y resto de una divisió")
num1 = int(input("Ingrese el número 1: "))
num2 = int(input("Ingrese el número 2: "))

if num2 > 0:
    if num1 > 0 :
        Cociente = num1/num2
        Resto = num1%num2

        print("Este es el resto 35"+str(Resto)+" Y este el cociente "+str(Cociente))
    elif num1 == 0:
        print("La operación no se pueden llevar a cabo")
elif num2 == 0:
    print("La operación no se puede llevar a cabo")

