try:
    pes_text=input("Decime tu peso en kg: ")
    pes_num=float(pes_text)
    alt_text=input("Decime tu altura en metros")
    alt_num=float(alt_text)
    imc=pes_num/(alt_num*alt_num)
    print(f"Tu IMC es: {imc}")
except ValueError:
    print("Ingrese un numero valido")
except ZeroDivisionError:
    print("Ingrese un numero que no sea cero")