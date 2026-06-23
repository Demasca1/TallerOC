import os
import time
import random
num=1
jugadores=[]
frutas=["Manzana", "Banana", "Naranja", "Frutilla"] 
try:
    jug=input("¿Cuantos jugadores son?: ")
    cantidad_jugador=int(jug)
    if cantidad_jugador ==1:
        print("No puedes jugar solo lamentablemente.")
    elif cantidad_jugador<=2:
        print("El maximo es de 15 personas y el minimo de 2")
    elif cantidad_jugador >15:
        print("No puedes jugar siendo mas de 15")
    else:
        for i in range (cantidad_jugador):
            Nombre=input(f"Introduce el nombre del jugador {num}: ")
            jugadores.append(Nombre)
            num=num+1
        impostor=random.choice(jugadores)
        palabra=random.choice(frutas)
        for i in range (cantidad_jugador):
            if impostor==jugadores[i]:
                print(f"Turno de {jugadores[i]}:")
                time.sleep(2)
                print("Eres el impostor")
                time.sleep(4)
                print("\033[F\033[K", end="")
            else:
                print(f"Turno de {jugadores[i]}:")
                time.sleep(2)
                print(f"Eres inocente, la palabra es: {palabra}")
                time.sleep(4)
                print("\033[F\033[K", end="")  
except ValueError:
    print("Ingrese un numero valido")
