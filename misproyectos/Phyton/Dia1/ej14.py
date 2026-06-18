try:
    num1_text=input("Dime cuanto te sacaste en la prueba ")
    num1_num=float(num1_text)
    if num1_num >6:
        print("Estas aprobado")
    elif num1_num < 6:
        print("Estas desaprobado")
    else:
        print("Estas aprobado")
except ValueError:
    print("Ingrese un numero valido")