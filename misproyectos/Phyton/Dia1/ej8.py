try:
    hotr_text=input("¿Cuantas horas de trabajo haces en el mes?:")
    hotr_num=float(hotr_text)
    tar_text=input("¿Cuanto te pagan por hora?:")
    tar_num=float(tar_text)
    sala=tar_num*hotr_num
    print(f"Tu salario es {sala}")
except ValueError:
    print("Ingrese un numero valido")