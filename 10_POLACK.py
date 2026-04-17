class Auto:
    posicion=0
    def __init__(self,motor,giro,motor_rapido,giro_rapido):
        self.motor=motor
        self.giro=giro
        self.motor_rapido=motor_rapido
        self.giro_rapido=giro_rapido
    def giro_brusco(self):
        self.giro=self.giro-3
        self.posicion+=self.giro_rapido
    def avance_rapido(self):
        self.motor=self.motor-4
        self.posicion+=self.motor_rapido
    def giro_normal(self):
        self.posicion+=self.giro
    def avance(self):
        self.posicion+=self.motor

largo_pista=100

motor_usuario=10
giro_usuario=8
rapido_usuario=30
giro_rapido_usuario=24

motor_1=20
giro_1=1
rapido_1=30
giro_rapido_1=120

motor_2=5
giro_2=16
rapido_2=60
giro_rapido_2=7.5


usuario=Auto(motor_usuario,giro_usuario,rapido_usuario,giro_rapido_usuario)
enemigo_1=Auto(motor_1,giro_1,rapido_1,giro_rapido_1)
enemigo_2=Auto(motor_2,giro_2,rapido_2,giro_rapido_2)


print("⋆✴︎˚｡⋆Bienvenido a la carrera!!⋆✴︎˚｡⋆")
carrera=True
while carrera: 
    avances_restantes=usuario.motor//4
    giros_restantes=usuario.giro//3
    print("\n----------⋆✴︎˚｡⋆----------")
    print("ACCIONES DE LA CARRERA")
    print("1)APRETAR EL ACELERADOR:Avanza a toda velocidad el auto (Abarca 30km de pista),pero causa un daño de -4 en el MOTOR")
    print("2)GIRO BRUSCO:Gira rapidamente en la pista,abarca muchos mas kilometros (24km de pista),pero da un -3 de daño al giro")
    print("3)SEGUIR:Avanza a velocidad normal,sin causar daño,abarca 10km")
    print("4)GIRO NORMAL:Gira de forma normal al encontrar una curva,abarca 8km")
    print("5)Consultar el ESTADO de mi AUTO")
    print("6)ABANDONAR la CARRERA")
    print("----------⋆✴︎˚｡⋆----------")
    op=int(input("\nIngrese el numero de la accion que desea tomar:"))

    if giros_restantes==0 or avances_restantes==0 or usuario.motor==0 or usuario.giro==0:
        print("\n----------⋆✴︎˚｡⋆----------")
        print("\nHas roto el auto :(")
        print("\nHas perdido la carrera, tus competidores han quedado... ")
        print("----------⋆✴︎˚｡⋆----------")
        if enemigo_1.posicion>enemigo_2.posicion:
            print(f"\nPRIMER LUGAR:Compañero 1 a {enemigo_1.posicion}KM")
            print(f"SEGUNDO LUGAR:Compañero 2 a {enemigo_2.posicion}KM de la carrera")
            print(f"TERCER LUGAR: UD a {usuario.posicion}KM de la carrera")
            print("----------⋆✴︎˚｡⋆----------")
        else:
            print(f"\nPRIMER LUGAR:Compañero 2 a {enemigo_2.posicion}KM")
            print(f"SEGUNDO LUGAR:Compañero 1 a {enemigo_1.posicion}KM de la carrera")
            print(f"TERCER LUGAR: UD a {usuario.posicion}KM de la carrera")
            print("----------⋆✴︎˚｡⋆----------")
        carrera=False
    else:

        if usuario.posicion>94:
            carrera=False
            print("\n----------⋆✴︎˚｡⋆----------")
            print("\nGanaste la carrera!!")
            print(f"\nPRIMER LUGAR: UD a {usuario.posicion}KM de la carrera")
            if enemigo_2.posicion>enemigo_1.posicion:
                    print(f"SEGUNDO LUGAR:Compañero 2 a {enemigo_2.posicion}KM de la carrera")
                    print(f"TERCER LUGAR: Compañero 1 a {enemigo_1.posicion}KM de la carrera")
                    print("----------⋆✴︎˚｡⋆----------")
            else:
                    print(f"SEGUNDO LUGAR: Compañero 1 a {enemigo_1.posicion}KM de la carrera")
                    print(f"TERCER LUGAR: Compañero 2 a {enemigo_2.posicion}KM de la carrera")
                    print("----------⋆✴︎˚｡⋆----------")

        elif enemigo_1.posicion>94 and enemigo_1.posicion>usuario.posicion and enemigo_1.posicion>enemigo_2.posicion:
                print("\n----------⋆✴︎˚｡⋆----------")
                print("\nGAME OVER")
                print("No has llegado a tiempo a la pista :c")
                print(f"\nPRIMER LUGAR:Compañero 1 a {enemigo_1.posicion}KM")
                if enemigo_2.posicion>usuario.posicion:
                    print(f"SEGUNDO LUGAR:Compañero 2 a {enemigo_2.posicion}KM de la carrera")
                    print(f"TERCER LUGAR: UD a {usuario.posicion}KM de la carrera")
                    print("----------⋆✴︎˚｡⋆----------")
                else:
                    print(f"SEGUNDO LUGAR: UD a {usuario.posicion}KM de la carrera")
                    print(f"TERCER LUGAR: Compañero 2 a {enemigo_2.posicion}KM de la carrera")
                    print("----------⋆✴︎˚｡⋆----------")
                carrera=False

        elif enemigo_2.posicion>94 and enemigo_2.posicion>usuario.posicion and enemigo_2.posicion>enemigo_1.posicion:
                print("\n----------⋆✴︎˚｡⋆----------")
                print("\nGAME OVER")
                print("No has llegado a tiempo a la pista :c")
                print(f"\nPRIMER LUGAR:Compañero 2 a {enemigo_2.posicion}KM")
                if enemigo_1.posicion>usuario.posicion:
                    print(f"SEGUNDO LUGAR:Compañero 1 a {enemigo_1.posicion}KM de la carrera")
                    print(f"TERCER LUGAR: UD a {usuario.posicion}KM de la carrera")
                    print("----------⋆✴︎˚｡⋆----------")
                else:
                    print(f"SEGUNDO LUGAR: UD a {usuario.posicion}KM de la carrera")
                    print(f"TERCER LUGAR: Compañero 1 a {enemigo_1.posicion}KM de la carrera")
                    print("----------⋆✴︎˚｡⋆----------")
                carrera=False
        else:
            if op==1 and avances_restantes>0:
                    usuario.avance_rapido()
                    print("\n----------⋆✴︎˚｡⋆----------")
                    print(f"UD AVANZA RAPIDAMENTE sobre la pista,esta a {usuario.posicion} KM /100KM en la pista")
                    print("\nSus competidores responden...")
                    enemigo_1.avance_rapido()
                    print(f"\nEl enemigo 1 avanza RAPIDAMENTE,queda a {enemigo_1.posicion} KM/100KM en la pista")
                    enemigo_2.giro_brusco()
                    print(f"El competidor 2 GIRA BRUSCAMENTE, esta a {enemigo_2.posicion} KM/100KM en la pista")
                    print("----------⋆✴︎˚｡⋆----------")
                    
            elif op==2 and giros_restantes>0:
                    usuario.giro_brusco()
                    print("\n----------⋆✴︎˚｡⋆----------")
                    print(f"UD da un GIRO BRUSCO sobre la pista,esta a {usuario.posicion} KM/100KM en la pista")
                    print("\nSus competidores responden...")
                    enemigo_1.avance()
                    print(f"\nEl enemigo 1 AVANZA,queda a {enemigo_1.posicion}KM/100KM en la pista")
                    enemigo_2.giro_brusco()
                    print(f"El enemigo 2 GIRO BRUSCAMENTE, queda a {enemigo_2.posicion}KM/100KM en la pista")
                    print("----------⋆✴︎˚｡⋆----------")
            elif op==3:
                    usuario.avance()
                    print("\n----------⋆✴︎˚｡⋆----------")
                    print(f"UD AVANZA sobre la pista, esta a {usuario.posicion}KM/100KM en la pista")
                    enemigo_1.avance_rapido()
                    print(f"\nEl enemigo 1 avanza RAPIDAMENTE,queda a {enemigo_1.posicion} KM/100KM en la pista")
                    enemigo_2.giro_brusco()
                    print(f"El competidor 2 GIRA BRUSCAMENTE, esta a {enemigo_2.posicion} KM/100KM en la pista")
                    print("----------⋆✴︎˚｡⋆----------")
            elif op==4:
                    usuario.giro_normal()
                    print("\n----------⋆✴︎˚｡⋆----------")
                    print(f"UD GIRA sobre la pista, esta a {usuario.posicion}KM/100KM en la pista")
                    print("Sus competidores responden...")
                    enemigo_1.avance()
                    print(f"\nEl enemigo 1 AVANZA,queda a {enemigo_1.posicion}KM/100KM en la pista")
                    enemigo_2.giro_brusco()
                    print(f"El enemigo 2 GIRO BRUSCAMENTE, queda a {enemigo_2.posicion}KM/100KM en la pista")
                    print("----------⋆✴︎˚｡⋆----------")
            elif op==5:
                    print("\n----------⋆✴︎˚｡⋆----------")
                    print("ESTADO DE SU AUTO:")
                    print(f"MOTOR:{usuario.motor}KM.")
                    print(f"{usuario.motor} AVANCES NORMALES RESTANTES")
                    print(f"{avances_restantes} AVANCES RAPIDOS RESTANTES")
                    print(f"GIRO:{usuario.giro}")
                    print(f"{giros_restantes} GIROS RAPIDOS RESTANTES")
                    print("----------⋆✴︎˚｡⋆----------")
            elif op==6:
                    print("\n----------⋆✴︎˚｡⋆----------")
                    print("\nGAME OVER")
                    print("ABANDONAS LA CARRERA :C")
                    print("\n----------⋆✴︎˚｡⋆----------")
                    carrera=False
            else:
                print("\n----------⋆✴︎˚｡⋆----------")
                print("\nPor favor, ingrese el numero de la opcion que este en el menú")
                print("\n----------⋆✴︎˚｡⋆----------")
                 


