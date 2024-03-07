cadena1 = "HOla soy jhon"
cadena2 = "Bienvenido carnal"

#CON dir se peuden ver todos loe metodos que se pueden utiliazr con una función 

#los metodos se ejecutan despues del . (punto)
# dato.metodo()

#METODOS CONVIERTEN UN VALOR
#UPPER convierto todo en mayuscula 
#Lower convierto todo en miniscula
#capitalize la primera letra en mayuscula (convierte todo en minuscula y despues toma la primera letra y la pasa a mayuscula)

resultado = cadena1.upper()
resultado2 = cadena1.lower()
resultado3 = cadena1.capitalize()

print(resultado)
print(resultado2)
print(resultado3)

#METODOS BUSCAN UN VALOR
#find busca una cadena en otra cadena si no hay coincidencia devuelve -1
#index hace lo mismo que la find, pero si no encuentra coincidencia arroja una escepción de error

busqueda_find=  cadena1.find("a")
print(busqueda_find)

busqueda_index = cadena1.index("a")

print(busqueda_index)

#METODOS QUE CONSULTAN UN VALOR 

#isnumeric si es numerico devuelve true
#isalplha si es alfanumerico devuelve true (los cuenta con caracteres que van de la a - z... los espacios no cuentan)

es_numerico= cadena1.isnumeric()

print(es_numerico)

#Count devuelve la cantidad de veces que coincida una cadana dentro de otra cadena 
#len cuenta la cantidad de caracteres en la cadena (es una función))

contar_cincidencia = cadena1.count("a")

print(contar_cincidencia)

contar_caracterres = len(cadena1)

print(contar_caracterres)


#startswinth si una cadena emoieza con otra cadena dada
# endswith si una cadena termina con otra cadena dada

empieza_con = cadena1.startswith("H")

print(empieza_con)

termina_con = cadena1.endswith("f")

print(termina_con)


#replace reemplaza un valor de la cadena dada por otra dada
#split separa cadenas con la cadena que se le pase (debe tener un indicativo de donde referenciarse para separar la lista)

cadena_nueva=cadena1.replace("la","lulo")

print(cadena_nueva)

cadena3 = "WEHAMMER IS THE REAL STORY"
cadena_separada = cadena3.split(",")

print(cadena_separada)
