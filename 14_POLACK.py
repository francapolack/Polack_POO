class Torre:
    salud=30
    danio_hecho=0
    def __init__(self,ataque1,ataque2,curar):
        self.ataque1=ataque1
        self.ataque2=ataque2
        self.curar=curar
    def ataqueuno(self):
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print("La TORRE se defiende..")
        print(f"Le lidia un {self.ataque1} de DAÑO al ENEMIGO")
        print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
    def ataquedos(self):
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print("La TORRE distrae...")
        print("Y ATACA")
        print(f"Le lidia un {self.ataque2} de DAÑO al ENEMIGO")
        print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
    def curamiento(self):
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print("La TORRE se cura...")
        self.salud+=self.curar
        print(f"Y queda con {self.salud}/30 de VIDA")
        print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
    def estado(self):
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print(f"SALUD de la TORRE:{self.salud}")
        print(f"DAÑO HECHO a la TORRE:{self.danio_hecho}")
        print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")

class Ataques():
    salud=40
    def ataqueuno(self):
        self.ataque1=10
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print("El ENEMIGO ataca..")
        print(f"Lidia un {self.ataque1} de DAÑO a la TORRE")
        print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
    def ataquedos(self):
        self.ataque2=20
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print("El ENEMIGO ataca...")
        print(f"Lidia un {self.ataque2} de DAÑO a la TORRE")
        print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
    def ataquetres(self):
        self.ataque3=5
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print("El ENEMIGO ataca..")
        print(f"Lidia un {self.ataque3} de DAÑO a la TORRE")
        print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")


torre1=Torre(10,5,10)
enemigo=Ataques()

print("La TORRE esta siendo ATACADA")
pelea=True
while pelea:
    if torre1.salud<1:
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print("GAME OVER")
        print("La TORRE ha CAIDO")
        print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        pelea=False
    elif enemigo.salud<1:
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print("FELICIDADES!!")
        print("Has defendido la TORRE")
        print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        pelea=False
    else:
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print(f"1)ATAQUE 1:Lidia {torre1.ataque1} de DAÑO al enemigo")
        print(f"2)ATAQUE 2:Lidia {torre1.ataque2} de DAÑO al enemigo")
        print(f"3)CURAR:Reestablece 10 puntos a la SALUD de la TORRE")
        print("4)CONSULTAR el ESTADO de la TORRE")
        print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        op=int(input("Ingrese el numero de la accion que quiere realizar:"))
        if op==1:
            torre1.ataqueuno()
            enemigo.salud-=torre1.ataque1
            enemigo.ataquetres()
            torre1.danio_hecho+=enemigo.ataque3
            torre1.salud-=enemigo.ataque3
        elif op==2:
            torre1.ataquedos()
            enemigo.salud-=torre1.ataque2
            enemigo.ataqueuno()
            torre1.danio_hecho+=enemigo.ataque1
            torre1.salud-=enemigo.ataque1
        elif op==3:
            torre1.curamiento()
            enemigo.ataquedos()
            torre1.danio_hecho+=enemigo.ataque2
            torre1.salud-=enemigo.ataque2
        elif op==4:
            torre1.estado()
        else:
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            print("Ingrese el numero de una opcion que este en el menu")
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")


