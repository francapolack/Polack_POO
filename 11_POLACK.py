Ejercicio 11: BATALLA DE HECHICEROS
cada acción tiene consecuencias sobre los recursos disponibles del personaje, por lo que será necesario
administrarlos correctamente.
El enfrentamiento continúa hasta que uno de los participantes ya no pueda seguir luchando.

class Hechicero:
    def __init__(self,salud,mana,hechizo_1,hechizo_2):
        self.salud=salud
        self.mana=mana
        self.hechizo_1=hechizo_1
        self.hechizo_2=hechizo_2
    
    def curar(self):
        self.salud=self.salud+self.mana
    
    def hechizo_uno(self,nombre,danio):
        print(f"Hechizo {nombre} ejecutado!!")
        print(f"Lidia un {danio} de daño")
        print(f"Pero resta -2 a la SALUD")
        self.salud-=1

    def hechizo_dos(self,nombre2,danio2):
        daniomana=danio2//2
        print(f"Hechizo {nombre2} ejecutado!!")
        print(f"Lidia un {danio2} de daño")
        print(f"Pero resta un {daniomana} al MANA")
        self.mana-=daniomana

usuario_salud=15
usuario_mana=5
usuario_hechizo_1="Abracadabra"
usuario_danio_1=10
usuario_hechizo_2="Pata de Cabra"
usuario_danio_2=20


enemigo_salud=15
enemigo_mana=5
enemigo_hechizo_1="Hocus Pocus"
enemigo_danio_1=10
enemigo_hechizo_2="Pata de Rana"
enemigo_danio_2=20  

    