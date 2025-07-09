#Diccionario
precios_frutas = {
    'manzana': (1200, 1500, 1300),
    'platano': (800, 800, 900),  #TIENE REPETIDOS
    'cereza': (2500, 2800, 2700)
}

#precio unico para una fruta especifica
fruta_seleccionada = 'platano'
precios_unicos = set(precios_frutas[fruta_seleccionada])
print(f"Precios únicos para {fruta_seleccionada}: {precios_unicos}")

#lista completa
tipos_fruta = list(precios_frutas.keys())
print(f"Tipos de fruta disponibles: {tipos_fruta}")

#promedio de esa fruta
promedio = sum(precios_unicos) / len(precios_unicos)
print(f"Precio promedio de {fruta_seleccionada} (valores únicos): {promedio:.2f} pesos chilenos")