
class Hechicero:
    def __init__(self,salud,mana,hechizo_1,hechizo_2,danio1,danio2):
        self.salud=salud
        self.mana=mana
        self.hechizo_1=hechizo_1
        self.hechizo_2=hechizo_2
        self.danio=danio1
        self.danio2=danio2
    def curar(self):
        self.salud=self.salud+self.mana
        self.mana-=5
        
        
    
    def hechizo_uno(self):
        print(f"Hechizo {self.hechizo_1} ejecutado!!")
        print(f"Lidia un {self.danio} de DAÑO al ENEMIGO")
        print(f"Pero resta -2 a la SALUD")
        self.salud-=1

    def hechizo_dos(self):
        print(f"Hechizo {self.hechizo_2} ejecutado!!")
        print(f"Lidia un {self.danio2} de DAÑO al ENEMIGO")
        print(f"Pero resta un mitad al MANA")
        self.mana=self.mana//2

usuario_salud=15
usuario_mana=20
usuario_hechizo_1="ABRACADABRA"
usuario_danio_1=10
usuario_hechizo_2="PATA DE CABRA"
usuario_danio_2=5

enemigo_salud=15
enemigo_mana=5
enemigo_hechizo_1="HOCUS POCUS"
enemigo_danio_1=10
enemigo_hechizo_2="PATA DE RANA"
enemigo_danio_2=5

usuario=Hechicero(usuario_salud,usuario_mana,usuario_hechizo_1,usuario_hechizo_2,usuario_danio_1,usuario_danio_2)
enemigo=Hechicero(enemigo_salud,enemigo_mana,enemigo_hechizo_1,enemigo_hechizo_2,enemigo_danio_1,enemigo_danio_2)

print("Bienvenido a la BATALLA de HECHICEROS")
batalla=True
while batalla:
    if usuario.salud<1:
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print("GAME OVER")
        print("Has perdido la BATALLA de HECHICEROS :(")
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        batalla=False
    elif enemigo.salud==0:
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print("FELICIDADES!!")
        print("Has ganado la BATALLA de HECHICEROS")
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        batalla=False
    else:
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print(f"1)ATACAR con HECHIZO 1:{usuario_hechizo_1}:Lidia 10 de DAÑO al enemigo pero resta -2 a la SALUD")
        print(f"2)ATACAR con HECHIZO 2:{usuario_hechizo_2}:Lidia 20 de DAÑO al enemigo pero resta deja a la mitad al MANA")
        print(f"3)USAR MANA: Cura {usuario_mana} a la SALUD")
        print("4)CONSULTAR mi ESTADO")
        print("5)ABANDONAR la BATALLA")
        print("---------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        op=int(input("\nTu turno!! Ingrese el numero de la ACCION que desea realizar:"))
        if op==1:
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            enemigo.salud-=usuario_danio_1
            usuario.hechizo_uno()
            print("Tu enemigo responde...")
            usuario.salud-=enemigo_danio_2
            enemigo.hechizo_dos()
            print(f"{enemigo_hechizo_2} te lidia {enemigo_danio_2} de DAÑO")
            print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        elif op==2:
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            enemigo.salud-=usuario_danio_2
            usuario.hechizo_dos()
            print("Tu enemigo responde...")
            enemigo.curar()
            print(f"Curandose,tiene ahora {enemigo.salud} de VIDA")
            print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------") 
        elif op==3:
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            usuario.curar()
            print("Te CURAS")
            print(f"Quedas con {usuario.salud} de VIDA pero pierdes 5 de MANA")
            print("Tu enemigo responde...")
            usuario.salud-=enemigo_danio_1
            enemigo.hechizo_uno()
            print(f"{enemigo_hechizo_2} te lidia {enemigo_danio_1} de DAÑO")
            print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        elif op==4:
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            print(f"SALUD:{usuario.salud}/{usuario_salud}")
            print(f"MANA:{usuario.mana}/{usuario_mana}")
            print(f"CURACIONES RESTANTES:{usuario.mana}")
            print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        elif op==5:
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            print("GAME OVER")
            print("Has abandonado la batalla de hechiceros :(")
            print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            batalla=False
        else:
            print("Ingrese una opcion del menu")

    



    



    