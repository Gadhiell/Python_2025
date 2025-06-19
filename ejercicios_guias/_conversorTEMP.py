#el usuario ingresa los grados celsius
GC = float(input ("dime cual es la temperatura  del dia de hoy (En Celsius):"))

#Farenheit y Kelvin
GF = ( GC * 9/5) + 32
GK = ( GC + 273.15)

#imprimir resultados de conversiones
print(f"Esta es la temperatura en grados Fahrenheit: {round(GF, 2)}")
print(f"Y esta es la temperatura en grados Kelvin: {round(GK, 2)}")
