cambio_texto=100
try:
    cambio_num=int(cambio_texto)
    cantdol_text=input("¿Cuantos dolares desea cambiar?:")
    cantdol_num=int(cantdol_text)
    cambio_tot=cantdol_num*cambio_texto
    print(f"Te daremos {cambio_tot} pesos por {cantdol_num} dolares")
except ValueError:
    print("Ingrese un numero valido")