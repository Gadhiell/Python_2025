colores =  {"azul","rojo", "azul", "Verde"}
colorcitos = {"azul,naranjo"}

#imprimiendo el set colores
print(colores)

#agregando un nuevo elemento al set (metodo ADD)
colores.add("blanco")
print(colores)

#eliminando un elemnto del set
colores.discard("blanco")

#aplicando el metodo DIFFERENCE
diferencia = colores.difference(colorcitos)
print(diferencia)