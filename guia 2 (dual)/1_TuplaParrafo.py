"""Camilo y Karla"""

#Lee el texto ingresado
texto = str(input('Ingrese el texto: \n'))
if texto == "":
    raise ValueError ("el texto no puede estar vacio")

#Eliminar comas y puntos.
texto_sc = texto.replace(',', '')
texto_sp = texto_sc.replace('.', '')

#El texto ya en minúscula se guarda en una lista
lista_texto = texto_sp.split()

#Ahora pide ingresar la palabra a contar
palabra = str(input('Ahora ingrese una palabra para contar cuántas veces se repite en el texto: \n'))


if not palabra:  # Verificar si la palabra está vacía
    raise ValueError("esta seccion no puede estar vacia")

#Variable que cuenta cuántas veces se repitió la palabra ingresada
repeticion = lista_texto.count(palabra)

print(f'La palabra {palabra} se repite {repeticion} veces')