try:
    dias_text=input("Dame una cantidad de dias: ")
    dias_num=float(dias_text)
    totalsec=(dias_num * 24 * 60 * 60)
    print(f"Hay {totalsec} segundos en {dias_text}dias")
except ValueError:
    print("Ingrese un numero valido")
