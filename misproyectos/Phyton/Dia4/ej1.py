saldo=1000
pinpr=1234
def verificar_pin(pinin):
    if pinin==pinpr:
        return True
    else:
        print("Pin incorrecto")
        return False
def retirar_cantidad(montod,saldod):
    try:
        if montod<=saldod:
            saldod=saldod-montod
            print(f"Su saldo quedo en: {saldod}")
        elif montod>saldod:
            print("Fondos insuficientes")
    except ValueError:
        print("Ingresa un numero valido")
print("🏦 Bienvenido al Banco Python")
while True:
    try:
        input_pin = input("Ingrese su PIN: ")
        pinint=int(input_pin)
        break
    except ValueError:
        print("Ingrese numeros, no letras")
if verificar_pin(pinint):
    print("Acceso concedido. Saldo actual: ", saldo)
    try:
        montostr=input("¿Cuanto desea retirar?: ")
        monto = int(montostr)
        retirar_cantidad(monto,saldo)
    except ValueError:
        print("Ingrese un monto valido")