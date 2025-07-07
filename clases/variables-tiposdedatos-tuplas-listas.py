carrera = "Ingenieria civil informatica"
edad = 18
#La Funcion LEN() Cuenta los caracteres de la variable,incluyendo espacios
print (f"la palabra {carrera} tiene:", len(carrera), "caracteres")

#Valores Booleanos

Interruptor = True 
Ampolleta = False

print(Interruptor, Ampolleta)

#La Funcion Type() permite saber el tipo de dato que se utiliza
print(type(edad))

#Comparativa de Valores Logicos
print(1<10)
print(100<=20)
print(100==100)

#aparecen true o false dependiendo si hay algo dentro o no
print(bool(""))
print(bool(1))
print(bool(0))
print(bool(318983))


#las listas es agrupar variables y datos en un mismo conjunto
lista1 = ["camilo", 18, True]
print (lista1)

#Solo numeros
n = [1,2,3,4,5]

#Solo Strings
ramos = list(["Programacion", "Quimica", "POO", "Programacion"])

#Imprimir el elemento de la posicion asignada (NO el caracter)
print(ramos[0])

#Se puede usar count para ver la cantidad de veces que se repite un elemento
print(ramos.count("Programacion"))

#creando e instanciando una tupla

estudiantes = ("samir", "camilo", "vale", "Hector" )

#Funcion Index (ver su posicion de cada instancia)
print(estudiantes.index("camilo"))

#Metodo Sorted en tuplas (ordena elementos)
print(sorted(estudiantes))
      
#creacion de sets (No hay ni orden ni repeticion de elementos)
colores = {"Azul","rojo", "verde"}
print (colores)
 
 

#Funcion APPEND
ramos.append ("intro a la mate")

#modificar elementos a la lista

ramos [1] = "comunicacion" #la posicion se marca con los[]
print(ramos)

#otra forma de añadir elementos
ramos.insert(0,"algebra")

#eliminar el ultimo elemento de la lista
ramos.pop()
print(ramos)

#Ordenando elementos de la lista
ramos.sort
print(ramos)

#Ordenando elementos de una lista segun la cantido de caracteres
#Key es una propiedad del metodo sort y se pasa un valor que es el metodo len
ramos.sort(key=len)
print(ramos)

#ocupando el metodo extend (combinar una lista  a partir de otra)
ramitos = ["calculo" , "automatas"]
ramos.extend (ramitos)
print(ramos)