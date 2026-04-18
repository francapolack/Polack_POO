class Torre:
    salud=30
    danio_hecho=0
    def ataqueuno(self):
        self.ataque1=10
        print("La TORRE se defiende..")
        print(f"Le lidia un {self.ataque1} de DAÑO al ENEMIGO")
    def ataquedos(self):
        self.ataque2=15
        print("La TORRE distrae...")
        print("Y ATACA")
        print(f"Le lidia un {self.ataque2} de DAÑO al ENEMIGO")
    def curar(self):
        self.curar=10
        print("La TORRE se cura...")
        self.salud+=self.curar
        print(f"Y queda con {self.salud}/30 de VIDA")
    def estado(self):
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print(f"SALUD de la TORRE:{self.salud}")
        print(f"DAÑO HECHO a la TORRE:{self.danio_hecho}")

class Ataques():
    salud=40
    def ataqueuno(self):
        self.ataque1=20
        print("El ENEMIGO ataca..")
        print(f"Lidia un {self.ataque1} de DAÑO a la TORRE")
    def ataquedos(self):
        self.ataque2=25
        print("El ENEMIGO ataca...")
        print(f"Lidia un {self.ataque2} de DAÑO a la TORRE")
    def ataquetres(self):
        self.ataque3=15
        print("El ENEMIGO ataca..")
        print(f"Lidia un {self.ataque3} de DAÑO a la TORRE")


torre1=Torre()
enemigo=Ataques()

pelea=True
while pelea:
    if torre1.salud==0:
        print("GAME OVER")
        print("La TORRE ha CAIDO")
        pelea=False
    elif enemigo.salud==0:
        print("FELICIDADES!!")
        pelea=False
    else:
        enemigo.ataqueuno()
        print(f"1)ATAQUE 1:Lidia {torre1.ataque1} de DAÑO al enemigo")
        print(f"2)ATAQUE 2:Lidia {torre1.ataque2} de DAÑO al enemigo")
        print(f"3)CURAR:Reestablece 10 puntos a la SALUD de la TORRE")
        print("4)CONSULTAR el ESTADO de la TORRE")
        op=int(input("Ingrese el numero de la accion que quiere realizar:"))
        if op==1:
            torre1.ataqueuno()
            enemigo.salud-=torre1.ataque1
            enemigo.ataque3()
        elif op==2:
            torre1.ataquedos()
            enemigo.salud-=torre1.ataque2
            enemigo.ataque1()
        elif op==3:
            torre1.curar()
            enemigo.ataque2()
        elif op==4:
            torre1.estado()
        else:
            print("Ingrese el numero de una opcion que este en el menu")


