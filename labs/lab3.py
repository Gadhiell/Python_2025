#Letra A
Datos = {

5700000 : {
"Ciudad" : "Castro ",
"Temperatura" : 11.8,
"Precipitacion" : 2000,
"MesesLluviosos" : "",
"Clima" : 17},


5770000 : {
"Ciudad" : "Chonchi",
"Temperatura" : 8.3,
"Precipitacion" : 2800,
"Clima" : 8},



5790000 : {
"Ciudad" : "Quellon",
"Temperatura" : 10.2,
"Precipitacion" : 2950,
"Clima" : 11}
}
print (Datos)



#Letra B
try:
    TempCastro = Datos[5700000]["Temperatura"]
    if TempCastro > 10:
        Datos[5700000]["Temperatura"] = "Frio"
    elif TempCastro == 10 or 11 or 12 or 13 or 14 or 15:
        Datos[5700000]["Temperatura"] = "Templado"
    else: TempCastro > 15
    Datos[5700000]["Temperatura"] = "Calido"
except:
    Datos[5700000]["Temperatura"] = "Desconocida"




try:
    TempChonchi = Datos[5770000]["Temperatura"]
    if TempChonchi > 10:
        Datos[5770000]["Temperatura"] = "Frio"
    elif TempChonchi == 10 or 11 or 12 or 13 or 14 or 15:
        Datos[5770000]["Temperatura"] = "Templado"
    else: TempChonchi > 15
    Datos[5770000]["Temperatura"] = "Calido"
except:
    Datos[5770000]["Temperatura"] = "Desconocida"



try:
    TempQuellon = Datos[5790000]["Temperatura"]
    if TempQuellon > 10:
        Datos[5790000]["Temperatura"] = "Frio"
    elif TempQuellon == 10 or 11 or 12 or 13 or 14 or 15:
        Datos[5790000]["Temperatura"] = "Templado"
    else: TempQuellon > 15
    Datos[5790000]["Temperatura"] = "Calido"
except:
    Datos[5790000]["Temperatura"] = "Desconocida"


print(TempCastro)
print(TempChonchi)
print(TempQuellon)


#Letra E
lluviasCA = Datos[5700000]["Precipitacion"]
lluviasCH = Datos[5770000]["Precipitacion"]
lluviasQU = Datos[5790000]["Precipitacion"]

print("el total de precipicaciones registradas es de:", lluviasCA + lluviasCH + lluviasQU)