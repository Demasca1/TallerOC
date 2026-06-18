try:
    num=input("Dame un numero entero: ")
    num_num=int(num)
    num_poi=num_num%2
    if num_poi == 0:
        print("Su numero es par")
    else:
        print("Su numero es impar")
except ValueError:
    print("Ingrese un numero valido")
