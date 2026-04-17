Cada acción influirá en el desempeño del vehículo, afectando su avance en la pista. Mientras tanto, los demás
competidores avanzarán automáticamente. El programa debe permitir observar la evolución de la carrera y
determinar el resultado final.

class Auto:
    def __init__(self,motor,giro):
        self.motor=motor
        self.giro=giro

motor_usuario=10
giro_usuario=8

motor_1=20
giro_1=1

motor_2=5
giro_2=6


usuario=Auto(motor_usuario,giro_usuario)
enemigo_1=Auto(motor_1,giro_1)
enemigo_2=Auto(motor_2,giro_2)

carrera=True
while carrera:



