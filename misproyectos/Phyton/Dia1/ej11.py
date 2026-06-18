try:
    num1_text=input("Decime el primer numero para dividir ")
    num1_num=float(num1_text)
    num2_text=input("Decime el segundo numero para dividir ")
    num2_num=float(num2_text)
    res=num1_num/num2_num
    print(f"El resultado es: {res}")
except ValueError:
    print("Ingrese un numero valido")
except ZeroDivisionError:
    print("Ingrese un numero que no sea cero")