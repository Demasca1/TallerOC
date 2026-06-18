try:
    gracel_text=input("¿Cuantos grados celsius hacen:")
    gracel_num=float(gracel_text)
    gra_far=(gracel_num * 9/5) + 32
    print(f"Hacen {gra_far} grados Fahrenheit")
except ValueError:
    print("Ingrese un numero valido")