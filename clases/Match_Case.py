#algo aparte
#importando una bibliteca (funciones adicionales)
from colorama import init, Fore
init()

#ejemplo de menu de comida rapida
print ("------MENU------")
print ("1.Hamburguesa")
print ("1.Pizza")
print ("1.Completo")

opcion = input("elige una opcion(1,2,3): ")

#elegir alternativas dependiendo de que opcion elija el usuario
match opcion:
    case "1" :
        print("elegiste hamburguesa,su precio es de $5500")
    case "2" :
        print("elegiste pizza,su precio es de $7000")
    case "3" :
        print("elegiste completo,su precio es de $2500")
    case _ :
        print("opcion invalida")

#determinar estacion segun el mes
mes = input("elige el numero de mes en que estamos")
match mes:
    case 12|1|2:
        print("verano")
    case 3|4|5:
        print("otoño")
    case 6|7|8:
        print("invierno")
    case 9|10|11:
        print("primaver")
    case _:
        print("mes incorrecto")

#Patrones Compuestos
x = [1,2,3]
match x:
    case [a,b,c]:
        print(f"elementos de la lista x; {a},{b},{c}")

datos = {
    "nombre": Camilo",
    "edad": 18
        }

