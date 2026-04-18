class Torre:
    salud=30
    danio_hecho=0
    def ataqueuno(self):
        self.ataque1=10
        print("La TORRE se defiende..")
        print(f"Le lidia un {self.ataque1} de DAÑO")
    def ataquedos(self):
        self.ataque2=15
        print("La TORRE distrae...")
        print("Y ATACA")
        print(f"Le lidia un {self.ataque2} de DAÑO")
    def estado(self):
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print(f"SALUD de la TORRE:{self.salud}")
        print(f"DAÑO HECHO a la TORRE:{self.danio_hecho}")

class Jugador():
    salud=25
    def ataqueuno(self):
        self.ataque1=20
        print("UD ataca..")
        print(f"Lidia un {self.ataque1} de DAÑO a la TORRE")
    def ataquedos(self):
        self.ataque2=25
        print("UD ataca...")
        print(f"Lidia un {self.ataque2} de DAÑO a la TORRE")

torre1=Torre()
usuario=Jugador()

pelea=True
while pelea:
    if usuario.salud==0:
        print("GAME OVER")
        print("La TORRE te ha derrotado")
        pelea=False
    elif torre1.salud==0:
        print("FELICIDADES!!6")
    else:
        
