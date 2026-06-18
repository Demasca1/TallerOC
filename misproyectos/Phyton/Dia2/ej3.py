try:
    num=input("Introduce un numero: ")
    num_num=float(num)
    vuelta=1
    for multi in range(1,11):
        mul=num_num*vuelta
        vuelta=vuelta+1
        print(f"La tabla de su numero por {multi} es: {mul}") 
except ValueError:
    print("Ingrese un numero valido")