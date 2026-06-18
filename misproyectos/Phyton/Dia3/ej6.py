try:
    decus=input("Decime el radio del circulo:")
    decusf=float(decus)
    def areacirculo (radio):
        res=radio*radio*3.1416
        return res
    areacirculo(decusf)
    print(f"El area del circulo es de {areacirculo(decusf)}")
except ValueError:
    print("Ingrese un numero valido")