# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

#payaso pesa 112 g
#muñeca 75 g

num_Payaso = int(input("Ingrese el número de payasos vendidos en el ultimo pedido: "))
num_Muñeca = int(input("Ingrese el número de muñecas vendidos en el ultimo pedido: "))

paq_payaso = num_Payaso*112
paq_muñeca = num_Muñeca*75

print("Ese es el total del peso del próximo pedido")
print("Paquete de payasos = ",paq_payaso)
print("Paquete de muñecas = ",paq_muñeca)



