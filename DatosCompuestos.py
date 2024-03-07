
#creando una lista (se puede modificar)
lista = ["lucas perez", "canal", True, 1.67]

#creando una tupla (no se puede modificar)
tupla={"lucas perez", "canal", True, 1.67}

#esto es valido
lista[3] = "maquinista"

#esto no es vlaido 
#tupla[2]= "maquinola" 

#creando un set
#no se peude llamar a los elementos por su indice
conjunto={"pedro ortiz", "majito", True, 1.97}


#creando un diccionario 
# key : value
diccionario = {
    'nombre' : "lucas dalto",
    'canal' : "saoy dalto",
    'esta_emocionado' : True,
    'altura' : 1.84,
    'dato_duplicado' : "saoy dalto"
}

print(lista)
print(conjunto)
print(diccionario['nombre'])