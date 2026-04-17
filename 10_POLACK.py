Mientras tanto, los demás competidores avanzarán automáticamente. El programa debe permitir 
observar la evolución de la carrera y
determinar el resultado final.
#Profe tenga piedad sobre mis parametros posta no se nada sobre autos
class Auto:
    posicion=0
    def __init__(self,motor,giro,motor_rapido,giro_brusco):
        self.motor=motor
        self.giro=giro
        self.motor_rapido=motor_rapido
        self.giro_brusco=giro_brusco
    def giro_brusco(self):
        self.giro=self.giro-3
        self.posicion+=self.giro_brusco
    def avance_rapido(self):
        self.motor=self.motor-4
        self.posicion+=self.avance_rapido
    def giro(self):
        print("Has girado en la pista")
        self.posicion+=self.motor
    def avance(self):
        print("Avanzas en la pista!!")
        self.posicion+=self.giro

largo_pista=100

motor_usuario=10
giro_usuario=8

motor_1=20
giro_1=1

motor_2=5
giro_2=16


usuario=Auto(motor_usuario,giro_usuario)
enemigo_1=Auto(motor_1,giro_1)
enemigo_2=Auto(motor_2,giro_2)

carrera=True
while carrera:
    print("Bienvenido a la carrera!!")
    print("ACCIONES DE LA CARRERA")
    print("1)APRETAR EL ACELERADOR:Avanza a toda velocidad el auto (Abarca 30km de pista),pero causa un daño de -4 en el MOTOR")
    print("2)GIRO BRUSCO:Gira rapidamente en la pista,abarca muchos mas kilometros (24km de pista),pero da un -3 de daño al giro")
    print("3)SEGUIR:Avanza a velocidad normal,sin causar daño,abarca 10km")
    print("4)GIRO NORMAL:Gira de forma normal al encontrar una curva,abarca 8km")
    print("5)Consultar el ESTADO de mi AUTO")
    print("6)ABANDONAR la CARRERA")
    op=int(input("Ingrese el numero de la accion que desea tomar"))
    if usuario.posicion==100 and enemigo_1.posicion<100 and enemigo_2.posicion<100:
        print("Ganaste la carrera!!")
        carrera=False
    if op==1:
        usuario.giro_brusco
        print(f"UD da un GIRO BRUSCO sobre la pista,esta a {usuario.posicion} KM en la pista")
        print("Sus competidores responden...")
        if enemigo_1.posicion<50 and enemigo_2<50:
            enemigo_1.avance_rapido()
            print(f"El enemigo 1 avanza RAPIDAMENTE,queda a {enemigo_1.posicion} KM en la pista")
            enemigo_2.giro_brusco()
            print(f"El competidor 2 GIRA BRUSCAMENTE, esta a {enemigo_2.posicion} KM en la pista")
        elif enemigo_1.posicion>=50 and enemigo_2>=50:
            enemigo_1.avance()
            print(f"El enemigo 1 AVANZA,queda a {enemigo_1.posicion}KM de la carrera")
            enemigo_2.avance()
            print(f"El enemigo 2 ")





