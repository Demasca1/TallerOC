try:
    num1_text=input("Decime el primer numero ")
    num1_num=float(num1_text)
    if num1_num>0:
        print("Su numero es positivo")
    elif num1_num<0:
        print("Su numero es negativo")
    else:
        print("Su numero es 0")
except ValueError:
    print("Ingrese un numero valido")