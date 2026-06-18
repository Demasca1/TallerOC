saldo=1000
repetir= True
def retirar_monto(monto):
    if monto<=saldo:
        saldoac=saldo-monto
        print(f"se retiro el monto deseado, su saldo quedo en ${saldoac}") 
        repetir=False
        return saldoac
    elif monto>saldo:
        print(f"Fondos insuficientes, su saldo sigue en:${saldo}")
        repetir=True
        return -1
def ver_mon(pin):
    if pin==1234:
        return True
    else:
        return False
try:
    for i in range(3):
        pinf=input("Introduce tu pin: ")
        pinfn=int(pinf)
except ValueError:
    print("Error, introduce un pin valido")
while repetir == True:
            try:
                retirar=input("Ingrese cuanto quiere retirar: ")
                retirarn=int(retirar)

            except ValueError:
                print("Error, ingrese un numero valido.")
retirar_monto(retirarn)
ver_mon(pinfn)