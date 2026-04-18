from random import randint
cofres_abiertos=[]
cofres_no_abiertos=7
class Cofre:
     estado="Cerrado"
     def __init__(self,monedas):
          self.monedas=monedas

i=0
ganancias=0

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
            exploracion=False
    else:
        if op==1:
            print("Explorando...")
            print(f"Ha aparecido el cofre {i}")
            i+=1
            print("Que desea hacer?")
            print("1)Abrir el cofre")
            print("2)Seguir explorando")
            opp=int(input("Ingrese su accion:"))
            if opp==1:
                abierto+=1
                cofre=Cofre(randint(1,1000))
                print(cofre.monedas)
                cofre.estado="Abierto"
                cofres_no_abiertos-=1
                cofres_abiertos.append(f"Cofre {i}")
                cofres_abiertos.append(cofre.monedas)
                ganancias+=cofre.monedas

            elif opp==2:
                print("Deja el cofre y sigue explorando...")

        




