try:
    n1=input("Dime un numero para el primero: ")
    n1f=float(n1)
    n2=input("Dime un numero para el segundo: ")
    n2f=float(n2)
    n3=input("Dime un numero para el tercero: ")
    n3f=float(n3)
    def numero_mayor (num1,num2,num3):
        if num1> num2 and num1>num3:
            print(f"El mas grande es: {num1}")
        elif num2> num1 and num2>num3:
            print(f"El mas grande es: {num2}")
        if num3>num2 and num3>num1:
            print(f"El mas grande es:{n3f}")
    numero_mayor (n1f,n2f,n3f)
except ValueError:
    print("Ingrese un numero valido")