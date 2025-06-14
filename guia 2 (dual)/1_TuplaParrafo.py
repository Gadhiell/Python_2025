"""Camilo y Karla"""

#Lee el texto ingresado
texto = str(input('Ingrese el texto: \n'))

#Se pasa todo el texto a minúscula
texto_min = texto.lower()

#El texto ya en minúscula se guarda en una lista
lista_texto = texto_min.split()

#Ahora pide ingresar la palabra a contar
palabra = str(input('Ahora ingrese una palabra para contar cuántas veces se repite en el texto: \n'))

#La palabra ingresada se guarda en minúscula todas sus letras
palabra_min = palabra.lower()

#Variable que cuenta cuántas veces se repitió la palabra ingresasa
repeticion = lista_texto.count(palabra_min)

print(f'La palabra {palabra} se repite {repeticion} veces')
