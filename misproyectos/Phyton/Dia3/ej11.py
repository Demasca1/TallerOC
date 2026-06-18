try:
    edus=input("Decime tu edad: ")
    edusf=int(edus)
    def puede_votar(edad):
        if edad>18:
            print("Podes votar")
        elif edad<18:
            print("Aun no puedes votar")
        else:
            print("Puedes votar")
    puede_votar(edusf)
except ValueError:
    print("Ingrese un numero valido")
except ZeroDivisionError:
    print("Ingrese un numero que no sea cero")