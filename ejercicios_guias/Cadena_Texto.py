# A. Ingresar una frase de máximo 30 caracteres
totalTXT = input("Ingresa una frase (solo se tomarán 30 caracteres): ")
texto = totalTXT[:30]

# B. Generar dos nuevas variables: mayúsculas y minúsculas
mayus = texto.upper()
minus = texto.lower()

print("Longitud de la frase original:", len(totalTXT))
print("Versión en mayúsculas: ", mayus)
print("Versión en minúsculas: ", minus)

TXTMinus = texto.count("a")
TXTMayus = texto.count("A")

print(" cantidad total de a minuscula: ", TXTMinus)
<<<<<<< HEAD
print(" cantidad total de A Mayuscula: ", TXTMayus)
=======
print(" cantidad total de A Mayuscula: ", TXTMayus)
>>>>>>> 253188bacab41794e0354d8754e4df642086a7d8
