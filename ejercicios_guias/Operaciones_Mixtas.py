N1 = int(input("ingresa un numero entero:"))
N2 = float(input("ahora un numero flotante(numero con decimales):"))
N3 = complex(input("y por ultimo un complejo (entero +- imaginario):"))

print ("entero:",N1)
print ("flotante:",N2)
print ("complejo:",N3)


Potencia = (N3 ** N1)
print("Potencia Compleja (Complejo^Entero):", Potencia)

Suma = (N3 + N2)
print("Suma Mixta (Complejo + Flotante):", Suma)

Producto = (N3 * N1)
print("Producto Mixto (Complejo * Entero):", Producto)

PotenciaComplex = abs(Potencia)
<<<<<<< HEAD
print("Potencia Compleja: {0:.3f}".format(PotenciaComplex))
=======
print("Potencia Compleja: {0:.3f}".format(PotenciaComplex))
>>>>>>> 253188bacab41794e0354d8754e4df642086a7d8
