class Personaje:
    vida=15
    def __init__(self,ataque,curar):
        self.ataque=ataque
        self.curar=curar
    def curamiento(self):
        self.curamiento=self.vida+self.curar
    
usuario=Personaje(5,3)
enemigo=Personaje(6,1)

menu=True
while menu:
    print("1)Consultar tu estado")
    print("2)Consultar el estado de tu enemigo")
    print("3)Atacar al enemigo")
    print("4)Curarse")
    print("5)Abandonar el duelo")
    op=int(input("Elija la opcion de menu que desea realizar:"))
    if op==1:
        print(f"-----------⋆⋅☆⋅⋆--------------")
        print("Tu estado es:")
        print(f"VIDA:{usuario.vida}/{Personaje.vida}")
        print(f"ATAQUE:{usuario.ataque}")
        print(f"CURAMIENTO:{usuario.curar}")
        print(f"-----------⋆⋅☆⋅⋆--------------")
    elif op==2:
        print(f"-----------⋆⋅☆⋅⋆--------------")
        print("El estado de tu enemigo es:")
        print(f"VIDA:{enemigo.vida}/{Personaje.vida}")
        print(f"ATAQUE:{enemigo.ataque}")
        print(f"CURAMIENTO:{enemigo.curar}")
        print(f"-----------⋆⋅☆⋅⋆--------------")
    elif op==3:
        print(f"-----------⋆⋅☆⋅⋆--------------")
        print(f"Atacas al enemigo y le haces {usuario.ataque} de daño!!")
        enemigo.vida=enemigo.vida-usuario.ataque
        print(f"Tu enemigo responde...")
        if enemigo.vida<10:
            print("Curandose...")
            print(f"Vida del enemigo al {enemigo.vida}/{Personaje.vida}")
            print(f"-----------⋆⋅☆⋅⋆--------------")
        else:
            print("Atacando!!")
            print(f"El enemigo te ataca y te da {enemigo.ataque} de daño")
            usuario.vida=usuario.vida-enemigo.ataque
            print(f"Tu vida ha quedado en {usuario.vida}/{Personaje.vida}")
            print(f"-----------⋆⋅☆⋅⋆--------------")
        if enemigo.vida==0:
            print(f"-----------⋆⋅☆⋅⋆--------------")
            print(f"FELICIDADES!!!")
            print(f"Has logrado derrotar al enemigo!!")
            print(f"-----------⋆⋅☆⋅⋆--------------")
            menu=False
        elif usuario.vida==0:
            print(f"-----------⋆⋅☆⋅⋆--------------")
            print("GAME OVER :(")
            print(f"Has sido derrotado por el enemigo")
            print(f"-----------⋆⋅☆⋅⋆--------------")
            menu=False
    elif op==4:
        print(f"-----------⋆⋅☆⋅⋆--------------")
        print("Curando...")
        usuario.curamiento()
        print(f"Vida:{usuario.vida}/{Personaje.vida}")
        print("El enemigo responde...")
        if enemigo.vida<10:
            print("Curandose...")
            print(f"Vida del enemigo al {enemigo.vida}/{Personaje.vida}")
            print(f"-----------⋆⋅☆⋅⋆--------------")
        else:
            print("Atacando!!")
            print(f"El enemigo te ataca y te da {enemigo.ataque} de daño")
            usuario.vida=usuario.vida-enemigo.ataque
            print(f"Tu vida ha quedado en {usuario.vida}/{Personaje.vida}")
            print(f"-----------⋆⋅☆⋅⋆--------------")
        if enemigo.vida==0:
            print(f"-----------⋆⋅☆⋅⋆--------------")
            print(f"FELICIDADES!!!")
            print(f"Has logrado derrotar al enemigo!!")
            print(f"-----------⋆⋅☆⋅⋆--------------")
            menu=False
        elif usuario.vida==0:
            print(f"-----------⋆⋅☆⋅⋆--------------")
            print("GAME OVER :(")
            print(f"Has sido derrotado por el enemigo")
            print(f"-----------⋆⋅☆⋅⋆--------------")
            menu=False
    elif op==5:
        print(f"-----------⋆⋅☆⋅⋆--------------")
        print("GAME OVER. Abandonaste el duelo!!")
        print(f"-----------⋆⋅☆⋅⋆--------------")
        menu=False
        



