import os
import time
import random
num=1
jugadores=[]
frutas=["Manzana", "Banana", "Naranja", "Frutilla"] 
jug=input("¿Cuantos jugadores son?: ")
cantidad_jugador=int(jug)
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
