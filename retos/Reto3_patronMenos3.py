#
N = 500
suma = 0
contador = 0


while N >= 101:
    print(N)
    suma += N
    contador += 1
    N -= 3

promedio = suma / contador  

# Imprimir los resultados
print("Suma total:", suma)
print("Promedio:", promedio)