import numeros

def preguntar():

    print("Bienvenido a Farmacia Mejia")

    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica")
        try: 
            mi_rubro = input("Elija su rubro: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("esa no es una opcion valida")
        else:
            break

    numeros.decorador(mi_rubro)

def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno?  [S] [N]").upper()
            ["S","N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()