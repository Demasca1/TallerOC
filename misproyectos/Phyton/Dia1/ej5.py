try:
    base_text=input("¿De cuanto es la base del rectangulo?:")
    base_num=float(base_text)
    alt_text=input("¿De cuanto es la altura del rectangulo?:")
    alt_num=float(alt_text)
    area=base_num*alt_num
    print (f"La base del rectangulo es:{area}")
except ValueError:
    print("Ingrese un numero valido")