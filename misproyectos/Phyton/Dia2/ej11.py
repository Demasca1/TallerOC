import random
secreto = int(random.randint(1, 100))
eleus=0
try:
    while eleus!=secreto:
        if eleus>secreto:
            print("Su numero es mayor al numero secreto")
        if eleus<secreto:
            print("Su numero es menor al numero secreto")   
        eleus=int(input(f"Su numero actual es {eleus},introduzca un numero: "))
    print("Felicitaciones, has ganado")
except ValueError:
    print("Ingrese un numero valido")
except ZeroDivisionError:
    print("Ingrese un numero que no sea cero")