try:
    not1_text=input("¿Cual fue tu primer nota?")
    not1_num=float(not1_text)
    not2_text=input("¿Cual fue tu segunda nota?")
    not2_num=float(not2_text)
    not3_text=input("¿Cual fue tu tercera nota?")
    not3_num=float(not3_text)
    prom=(not1_num+not2_num+not3_num)/3
    print(f"Tu promedio es de {prom}")
except ValueError:
    print("Ingrese un numero valido")