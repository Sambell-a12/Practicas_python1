print("A continuacion vas a crear una matriz e ingresar datos en una amtriz ")

fil = int(input("Ingrese el número de filas =)"))
Col = int(input("Ingrese el número de columnas =)"))

matriz = []

for i in range(fil):
    fil = []
    for j in range(Col):
        #La ´f´ permite realizar una concatenación de cadenas más rapida en un solo lado 
        valor = int(input(f"Ingrese el valor para la fila {i+1}, columna {j+1}: "))
        fil.append(valor)
    matriz.append(fil)


#Imprimir la matriz 

print("La matriz ingresada es: ")
for fil in matriz:
    print(fil)


# para una clase la primera que aparaece es el objeto a utilizar al momento de llamarla o instanciarla 



