palabra= input("Introduce una palabra: ")
vocales=0
for letra in palabra:
    print(f"La primer letra es: {letra}")
    if letra in "aAeEiIoOuU":
        vocales=vocales+1
print(f"La cantidad de vocales es {vocales}")
