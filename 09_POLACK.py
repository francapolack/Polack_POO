from random import randint
cofres_ganancias=[]
cofres_no_abiertos=7
moneditas=0
joyitas=0
brillan=0
#añadir mas tesoros???
class Cofre:
     estado="Cerrado"
     def __init__(self,monedas,joyas,brillantes):
          self.monedas=monedas
          self.joyas=joyas
          self.brillantes=brillantes

i=1
print("Bienvenido a la Cueva de los tesoros")
exploracion=True
while exploracion:
    print("1)Explorar")
    print("2)Ver mis cofres")
    print("3)Ver mis ganancias")
    print("4)Abandonar la cueva")
    op=int(input("Ingrese la opcion del menu que desea ejecutar:"))
    if i>8:
            print("GAME OVER")
            print("FIN DE LA CUEVA")
            print(f"Ya no quedan cofres para buscar :(")
            print(f"COFRES ABIERTOS:{i}///GANANCIAS TOTALES:{ganancias}")
            exploracion=False
    else:
        if op==1:
            print("Explorando...")
            print(f"Ha aparecido el cofre {i}")
            print("Que desea hacer?")
            print("1)Abrir el cofre")
            print("2)Seguir explorando")
            opp=int(input("Ingrese su accion:"))
            if opp==1:
                cofre=Cofre(randint(0,1000),randint(0,6),randint(0,300))
                print(cofre.monedas)
                cofre.estado="Abierto"
                cofres_no_abiertos-=1
                cofres_ganancias.append(f"COFRE {i}")
                cofres_ganancias.append(f"MONEDAS del COFRE {i}: {cofre.monedas}")
                cofres_ganancias.append(f"JOYAS del COFRE {i}: {cofre.joyas}")
                cofres_ganancias.append(f"BRILLANTES del COFRE {i}: {cofre.brillantes}")
                ganancias+=cofre.monedas
                joyitas+=cofre.joyas
                brillan+=cofre.brillantes
                i+=1
            elif opp==2:
                print("Deja el cofre y sigue explorando...")
                i+=1
        elif op==2:
             print("-------------------------------")
             for x in range(0,len(cofres_ganancias)):
                  print(f"\n{cofres_ganancias[x]}---")
             print("-------------------------------")
        elif op==3:
            print("GANANCIAS TOTALES")
            print(f"MONEDAS:{moneditas}")
            print(f"JOYAS:{joyitas}")
            print(f"BRILLANTES:{brillan}")
        elif op==4:
             print("GAME OVER")
             print("Has abandonado la cueva :(")
             exploracion=False
        




