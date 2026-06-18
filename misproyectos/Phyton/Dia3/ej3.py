try:
    numcua=input("Ingresa un numero de un cuadrado:")
    numcuaf=float(numcua)
    def cuadrado(numero):
        multi=numcuaf*numcuaf
        return multi
    multi=cuadrado(numcuaf)
    print(f"El cuadrado de numero es {multi}")
except ValueError:
    print("Ingrese un numero valido")