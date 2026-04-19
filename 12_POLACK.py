

from random import randint
class escenario:
    def objeto(self,nombre,efecto):
        self.nombre=nombre
        self.efecto=efecto

i=1
inventario=[]
objetos_descartados=0
objetos_encontrados=0
objetos_usados=0


escenarios=["MONTAÑA","DESIERTO","BOSQUE"]
objetos=["Helado","Pocion de Agua","Pico de Hielo","Pocion de Arena","Arena Movediza","Pan","Pocion del Rio","Salmon","Hacha"]
efectos=["Hace NADA","Hace que el CLIMA mejore","AHUYENTA a todos los ENEMIGOS","Te hace mas FELIZ"]


aventura=True
while aventura:
    if objetos_encontrados>7:
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print("FELICIDADES!!")
        print("Has encontrado TODOS los objetos de los escenarios!!")
        print(f"Objetos encontrados en TOTAL:{objetos_encontrados}")
        print(f"Objetos DESCARTADOS:{objetos_descartados}")
        print(f"Objetos USADOS:{objetos_usados}")
        print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        aventura=False
    else:
        print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        print("1)Explorar")
        print("2)Ver mis OBJETOS")
        print("3)Usar un OBJETO")
        print("4)Descartar333333333333333333333333333333333333333 un OBJETO")
        print("5)Abandonar la AVENTURA")
        op=int(input("Ingrese el número de la opción que desea realizar:"))
        print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
        if op==1:
            escenario_chance=randint(0,2)
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            print(f"ESCENARIO:{escenarios[escenario_chance]}")
            objeto=objetos[randint(0,8)]
            efecto=efectos[randint(0,3)]
            escenarioo=escenario()
            escenarioo.objeto(objeto,efecto)
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            print(f"Te encuentras un {escenarioo.nombre}")
            print(f"EFECTO del OBJETO {escenarioo.nombre}:{escenarioo.efecto}")
            objetos_encontrados+=1
            op=str(input("Deseas GUARDARLO? SI/NO:"))
            if op=="si" or op=="SI":
                print(f"Te GUARDAS el {escenarioo.nombre}")
                inventario.append(f"OBJETO {i}:{escenarioo.nombre}")
                inventario.append(f"EFECTO DEL OBJETO:{escenarioo.efecto}")
                i+=1
            elif op=="no" or op=="NO":
                objetos_descartados+=1
                print("Tiras el objeto y sigues explorando...")
                print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            i+=1
        elif op==2:
            for objeto in inventario:
                print(objeto)
        elif op==3:
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            op=int(input("Escribe el numero del objeto que deseas usar:"))
            print(f"USAS el objeto {inventario[op-1]}!!")
            print(f"{inventario[op]}")
            print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            objetos_usados+=1
            inventario[op]=""
            inventario[op-1]=""
        elif op==4:
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            op=int(input("Escribe el numero del objeto que deseas descartar:"))
            print(f"DESCARTAS el objeto {inventario[op-1]}!!")
            print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            objetos_descartados+=1
            inventario[op]=""
            inventario[op-1]=""
        elif op==5:
            print("\n--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            print("ABANDONAS LA AVENTURA :(")
            print("--------------✩₊˚.⋆☾⋆⁺₊✧--------------------")
            aventura=False            










