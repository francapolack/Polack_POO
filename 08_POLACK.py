class Personaje:
    vida=15
    def __init__(self,ataque,curar):
        self.ataque=ataque
        self.curar=curar

usuario=Personaje(5,3)
print(usuario.curar,usuario.ataque,usuario.vida)
enemigo=Personaje(6,1)
print(enemigo.vida,enemigo.curar,enemigo.ataque)

menu=True
while menu:
    print("op1,op2,op3")
    op=int(input("Elija la opcion de menu que desea realizar:"))
    if op==1:
            print("x")
    elif op==2:
            print("y")
    elif op==3:
          print("z")
    elif op==4:
        print("fin")
        menu=False
        



