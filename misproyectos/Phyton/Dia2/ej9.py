precios={
    "Manzana":100,
    "Banana":50,
    "Naranja":80,
}
selus=input("Selecciona una fruta entre Manzana, Naranja o Banana: ")
kilus=int(input("Selecciona la cantidad de kilos que quieres:"))

precio={precios.get(selus)}
total=precio*kilus
print(f"El total de su compra es de:${total}")