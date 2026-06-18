try:
    pre_text=input("Dame el precio original de un producto: ")            
    pre_num=float(pre_text)
    por_text=input("Dame el porcentaje de descuento: ")
    por_num=float(por_text)
    destotal=pre_num/por_num
    pretotal=pre_num-destotal
    print(f"El descuento que se te hara es de: {destotal}")
    print(f"El precio total con descuento seria: {pretotal}")
except ValueError:
    print("Ingrese un numero valido")
except ZeroDivisionError:
    print("Ingrese un numero que no sea cero")