from random import randint
class Jugador:
    def __init__(self,punt):
        self.puntaje=punt
    def tiro(self):
        print("Tirando...")
        self.tiro1=randint(1,6)
        print(f"El dado da un valor de {self.tiro1}!")
        self.puntaje+=self.tiro1

    

usuario=Jugador(0)
jugador1=Jugador(0)
jugador2=Jugador(0)
ronditas=0
rondas=True

while rondas:
    if ronditas>3:
        print("\nJuego Terminado!")
        print("Los puntajes ganadores son...")
        if usuario.puntaje>jugador1.puntaje and usuario.puntaje>jugador2.puntaje:
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            print(f"PRIMER LUGAR:UD con {usuario.puntaje} PUNTOS!")
            if jugador1.puntaje>jugador2.puntaje:
                print(f"SEGUNDO LUGAR:JUGADOR 1 con {jugador1.puntaje} PUNTOS!")
                print(f"TERCER LUGAR:JUGADOR 2 con {jugador2.puntaje} PUNTOS!")
                print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            else:
                print(f"SEGUNDO LUGAR:JUGADOR 2 con {jugador2.puntaje} PUNTOS!")
                print(f"TERCER LUGAR:JUGADOR 1 con {jugador1.puntaje} PUNTOS!")
                print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        elif jugador1.puntaje>usuario.puntaje and jugador1.puntaje>jugador2.puntaje:
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            print(f"PRIMER LUGAR:JUGADOR 1 con {jugador1.puntaje} PUNTOS!")
            if usuario.puntaje>jugador2.puntaje:
                print(f"SEGUNDO LUGAR:UD con {usuario.puntaje} PUNTOS!")
                print(f"TERCER LUGAR:JUGADOR 2 con {jugador2.puntaje} PUNTOS!")
                print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            else:
                print(f"SEGUNDO LUGAR:JUGADOR 2 con {jugador2.puntaje} PUNTOS!")
                print(f"TERCER LUGAR:UD con {usuario.puntaje} PUNTOS!")
                print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        else:
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            print(f"PRIMER LUGAR:JUGADOR 2 con {jugador2.puntaje} PUNTOS!")
            if usuario.puntaje>jugador1.puntaje:
                print(f"SEGUNDO LUGAR:UD con {usuario.puntaje} PUNTOS!")
                print(f"TERCER LUGAR:JUGADOR 1 con {jugador1.puntaje} PUNTOS!")
                print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            else:
                print(f"SEGUNDO LUGAR:JUGADOR 1 con {jugador2.puntaje} PUNTOS!")
                print(f"TERCER LUGAR:UD con {usuario.puntaje} PUNTOS!")
                print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        rondas=False
    else:
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print(f"RONDA NUMERO {ronditas}!")
        print("Tira el Jugador 1...")
        jugador1.tiro()
        print("Tira el Jugador 2...")
        jugador2.tiro()
        op=str(input("UD desea tirar? SI/NO:"))
        print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        if op=="SI" or op=="si":
            usuario.tiro()
            print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        elif op=="NO" or op=="no":
            print("OK! Sigue el juego...")
            print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        ronditas+=1