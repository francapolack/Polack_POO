from random import randint
cofres_ganancias=[]
cofres_no_abiertos=8
moneditas=0
joyitas=0
brillan=0
cofres_abiertos=0
i=1
class Cofre:
     estado="Cerrado"
     def __init__(self,monedas,joyas,brillantes):
          self.monedas=monedas
          self.joyas=joyas
          self.brillantes=brillantes
print("----------⋆✴︎˚｡⋆----------")
print("Bienvenido a la Cueva de los tesoros")
print("----------⋆✴︎˚｡⋆----------")
exploracion=True
while exploracion:
    print("\n----------⋆✴︎˚｡⋆----------")
    print("1)Explorar")
    print("2)Ver mis cofres")
    print("3)Ver mis ganancias")
    print("4)Abandonar la cueva")
    print("----------⋆✴︎˚｡⋆----------")
    op=int(input("Ingrese la opcion del menu que desea ejecutar:"))
    
    if i>8:
            print("\n----------⋆✴︎˚｡⋆----------")
            print("GAME OVER")
            print("FIN DE LA CUEVA")
            print(f"Ya no quedan cofres para buscar :(")
            print("-----------------------------")
            print(f"\nCOFRES ABIERTOS:{cofres_abiertos}")
            print(f"MONEDAS TOTALES:{moneditas}")
            print(f"JOYAS TOTALES:{joyitas}")
            print(f"BRILLANTES TOTALES:{brillan}")
            print(f"\nCOFRES *NO* ABIERTOS:{cofres_no_abiertos}")
            print("-----------------------------")
            print("----------⋆✴︎˚｡⋆----------")
            exploracion=False
    else:
        if op==1:
            print("\n----------⋆✴︎˚｡⋆----------")
            print("Explorando...")
            print(f"Ha aparecido el cofre {i}")
            cofre=Cofre(randint(0,1000),randint(0,6),randint(0,300))
            print(f"Su ESTADO es:{cofre.estado}")
            print("Que desea hacer?")
            print("1)Abrir el cofre")
            print("2)Seguir explorando")
            print("----------⋆✴︎˚｡⋆----------")
            opp=int(input("Ingrese su accion:"))
            if opp==1:
                print("\n----------⋆✴︎˚｡⋆----------")
                print(f"MONEDAS ENCONTRADAS: {cofre.monedas}")
                print(f"JOYAS ENCONTRADAS: {cofre.joyas}")
                print(f"BRILLANTES ENCONTRADOS: {cofre.brillantes}")
                print("----------⋆✴︎˚｡⋆----------")
                cofre.estado="Abierto"
                cofres_no_abiertos-=1
                cofres_abiertos+=1
                cofres_ganancias.append(f"COFRE {i}")
                cofres_ganancias.append(f"MONEDAS del COFRE {i}: {cofre.monedas}")
                cofres_ganancias.append(f"JOYAS del COFRE {i}: {cofre.joyas}")
                cofres_ganancias.append(f"BRILLANTES del COFRE {i}: {cofre.brillantes}")
                moneditas+=cofre.monedas
                joyitas+=cofre.joyas
                brillan+=cofre.brillantes
                i+=1
            elif opp==2:
                print("\n----------⋆✴︎˚｡⋆----------")
                print("Deja el cofre y sigue explorando...")
                print("----------⋆✴︎˚｡⋆----------")
                i+=1
        elif op==2:
             print("\n----------⋆✴︎˚｡⋆----------")
             for x in range(0,len(cofres_ganancias)):
                  print(f"\n{cofres_ganancias[x]}")
             print("----------⋆✴︎˚｡⋆----------")
        elif op==3:
            print("\n----------⋆✴︎˚｡⋆----------")
            print("GANANCIAS TOTALES")
            print(f"MONEDAS:{moneditas}")
            print(f"JOYAS:{joyitas}")
            print(f"BRILLANTES:{brillan}")
            print("----------⋆✴︎˚｡⋆----------")
        elif op==4:
             print("\n----------⋆✴︎˚｡⋆----------")
             print("GAME OVER")
             print("Has abandonado la cueva :(")
             print("----------⋆✴︎˚｡⋆----------")
             exploracion=False
        




