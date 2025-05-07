"""Introduccion de Python"""

nombre = "Camilo"
apellido = "Chavez"


#print con variables y comas 
print("hello  mundo,mi nombre es", nombre, apellido)

#Operador De Concatenacion
print("hola otra vez,mi nombre es " + nombre  +  apellido)

#Print con F-Strings (Cadenas literales)
print (f"hola mi nombre es {nombre} {apellido}")

#Inicializando Multi Variables en una sola linea (NO RECOMENDADO)
ciudad, region , pais = "castro", "Los Lagos", "Chile"
print ("hola soy de {ciudad}, {region}, {pais}")