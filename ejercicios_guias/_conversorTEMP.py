#el usuario ingresa los grados celsius
GC = float(input ("dime cual es la temperatura  del dia de hoy (En Celsius):"))

#Farenheit y Kelvin
GF = ( GC * 9/5) + 32
GK = ( GC + 273.15)

#imprimir resultados de conversiones
print (f"esta es la temperatura en grados farenheit:",GF)
print (f"y esta es la temperatura en grados kelvin:",GK)