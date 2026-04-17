from random import randint
no_abierto=6
abierto=0
class Cofre:
    monedas=randint(1,100)
    estado="Cerrado"

print("Bienvenido a la Cueva de los tesoros...")
i=0
menu=True
while menu:
    print("1)Continuar explorando")
    print("2)Ver mis cofres")
    print("3)Ver mis ganancias")
    print("4)Abandonar la cueva")
    op=int(input("Ingrese la opcion del menu que desea ejecutar:"))
    if i>8:
            print(f"Ya no quedan cofres para buscar :(")
            menu=False
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
                cofre=Cofre()
                print(cofre.monedas)
                cofre.estado="Abierto"
                print(cofre.estado)
            elif opp==2:
                print("Deja el cofre y sigue explorando...")

        




