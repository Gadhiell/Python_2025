"""Camilo y Karla"""

#Lee el texto ingresado,verificando que no este vacio
texto = str(input('Ingrese el texto: \n'))
if texto == "":
    raise ValueError ("el texto no puede estar vacio")

#Eliminar comas y puntos.
texto_sc = texto.replace(',', '')
texto_sp = texto_sc.replace('.', '')

lista_texto = texto_sp.split()


<<<<<<< HEAD
#Ahora pide ingresar la palabra a contar,y verificar si esta vacio
palabra = str(input('Ahora ingrese una palabra para contar cuántas veces se repite en el texto: \n'))
if not palabra:
=======
#Ahora pide ingresar la palabra a contar,verificando que no este vacio
palabra = str(input('Ahora ingrese una palabra para contar cuántas veces se repite en el texto: \n'))
if palabra == "":
>>>>>>> 1b2bad09162803997fe302b8e99cfe3c3e76280e
    raise ValueError("esta seccion no puede estar vacia")

#Variable que cuenta cuántas veces se repitió la palabra ingresada
repeticion = lista_texto.count(palabra)

print(f'La palabra {palabra} se repite {repeticion} veces')
