"""Camilo y Karla"""

# Ingresar el numero para probar la formula
try:
    Num = int(input("Ingrese un numero entero: "))
except ValueError:
    print("No has ingresado un numero entero")
else:
    ImparInicial = 1

    # Acumular y almacenar impares en lista
    for i in range(1, Num + 1):
        suma = 0
        impar = []
        ImparInicial = 1  # Reiniciar para cada i

        # Sumar los siguientes impares consecutivos
        for _ in range(i):
            impar.append(ImparInicial)
            suma += ImparInicial
            ImparInicial += 2  # Aumentar el siguiente impar

        # Construir la cadena de impares
        C_Impar = " + ".join(map(str, impar))
        print(f"{i}^3 = {C_Impar} = {suma}")