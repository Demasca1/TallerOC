try:
    infus=input("cuantos minutos queres pasar a horas:")
    infusf=float(infus)
    def min_hor(minutos):
        resultado=(minutos//60)
        return resultado
    min_hor(infusf)
    mins=infusf%60
    print(f"En {infusf} minutos hay {min_hor(infusf)} horas y {mins} minutos")
except ValueError:
    print("Ingrese un numero valido")
except ZeroDivisionError:
    print("Ingrese un numero que no sea cero")