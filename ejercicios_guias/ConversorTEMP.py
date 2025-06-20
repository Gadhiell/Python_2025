#el usuario ingresa los grados celsius
GC = float(input ("dime cual es la temperatura  del dia de hoy (En Celsius):"))

#Farenheit y Kelvin
GF = ( GC * 9/5) + 32
GK = ( GC + 273.15)

#imprimir resultados de conversiones
print(f"Esta es la temperatura en grados Fahrenheit: {round(GF, 2)}")
<<<<<<< HEAD:ejercicios_guias/ConversorTEMP.py
print(f"Y esta es la temperatura en grados Kelvin: {round(GK, 2)}")
=======
print(f"Y esta es la temperatura en grados Kelvin: {round(GK, 2)}")
>>>>>>> 253188bacab41794e0354d8754e4df642086a7d8:ejercicios_guias/_conversorTEMP.py
