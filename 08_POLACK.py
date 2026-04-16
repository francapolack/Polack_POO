class Personaje:
    vida=15
    def __init__(self,ataque,curar):
        self.ataque=ataque
        self.curar=curar
    def curamiento(self):
        self.curamiento=self.vida+self.curar
    

usuario=Personaje(5,3)
print(usuario.curar,usuario.ataque,usuario.vida)
enemigo=Personaje(6,1)
print(enemigo.vida,enemigo.curar,enemigo.ataque)

menu=True
while menu:
    print("1)Consultar tu estado")
    print("2)Atacar al enemigo")
    print("3)Curarse")
    print("4)Abandonar el duelo")
    op=int(input("Elija la opcion de menu que desea realizar:"))
    if op==1:
        print("x")
    elif op==2:
        print(f"Atacas al enemigo y le haces {usuario.ataque} de daño!!")
            
    elif op==3:
        print("Curando...")
        usuario.curamiento()
        print(f"Vida:{usuario.vida}/{Personaje.vida}")
        print("El enemigo responde...")
        if enemigo.vida<10:
            print("Curandose...")
            print(f"Vida del enemigo al")
    elif op==4:
        print("GAME OVER. Abandonaste el duelo!!")
        menu=False
        



