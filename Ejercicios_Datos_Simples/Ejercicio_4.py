#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.


#print("¿Cuales fueron sus horas trabajadas?")

#Horas_Tra = input()

#print("Ingrese el valor de la hora de trabajo")

#Hora_Pagas = input()

#Pago = Hora_Pagas*Horas_Tra

#print("Su paga por trabajar"+ Horas_Tra +"horas es de"+Pago)

#CORRECCION----------------------------------------------------------------

Horas = float(input("Introduce tus horas de trabajo: "))
Coste = float(input("Ingrese lo que cobre por hora: "))
paga= Horas * Coste
print("Tu paga es",paga)