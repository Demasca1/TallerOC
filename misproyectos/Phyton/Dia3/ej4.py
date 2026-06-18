try:
    decus=input("Ingresa un numero: ")
    decusn=float(decus)
    def es_par(numero):
        poi=decusn%2
        return poi
    if es_par(decusn) == 0:
        print("True")
    else:
        print("False")
except ValueError:
    print("Ingrese un numero valido")
