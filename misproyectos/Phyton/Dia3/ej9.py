lista={
    100:10,
    50:5,
    25:15,
}
def calcular_precio_final(precio, descuent):
    res=(descuent*100)/precio
    tot=precio-res
    return tot
try:
    selus=input("Elige un precio entre 100,50 y 25: ")
    selusf=float(selus)
    if selusf==100:
        descuento=10
    elif selusf==50:
        descuento=5
    if selusf==25:
        descuento=15
    calcular_precio_final(selusf,descuento)
    print(f"El precio final es: ${calcular_precio_final(selusf,descuento)}")
except ValueError:
    print("Ingrese un numero valido")