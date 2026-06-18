try:    
    num1_text=input("Decime el primer numero ")
    num1_num=float(num1_text)
    num2_text=input("Decime el segundo numero ")
    num2_num=float(num2_text)
    if num1_num>num2_num:
        print(f"El primer numero que vale {num1_num} es mayor que el segundo que vale {num2_num}")
    elif num2_num>num1_num:
        print(f"El segundo numero que vale {num2_num} es mayor que el primero que vale {num1_num}")
    else:
        print(f"Ambos numeros valen lo mismo: {num1_num}")
except ValueError:
    print("Ingrese un numero valido")
except ZeroDivisionError:
    print("Ingrese un numero que no sea cero")