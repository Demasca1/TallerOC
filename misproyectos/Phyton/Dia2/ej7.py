suma_total=0
numsec=0
try:
    while numero!= 0:
        numero=int(input("Elige"))
        if numero!=0:
            numsec=numsec+numero
        else:
            print("Casi, sigue intentado")
            suma_total=suma_total+numero
        print(f"Adivinaste el numero que era {numsec}, felicidades")
except ValueError:
    print("Ingrese un numero valido")