#creando diccionario dentro de los diccionarios se pueden agregar distintos tipos de datos estructurados
Inventario = {
    "nombre": "carlos",
    "apellido": "santana",
    "edad": 50,
    "ciudad": "quellon",
    "consultas": [14,20,40],
    "diagnostico": ("resfrio")
    
}

print(type(paciente))

#Otra forma de declarar diccionario
medico = dict(
    nombre = "samir",
    apellido = "arana",
    
    edad = 20,
    especialidad = "neurologo"
    )
#impresion de diccionario
print(paciente)
print(medico)

#consultando un elemento a traves de la clave de diicionario
print (medico["nombre"])

#eliminando una clave del diccionario (metodo del)
del(paciente["nombre"])
print(paciente)