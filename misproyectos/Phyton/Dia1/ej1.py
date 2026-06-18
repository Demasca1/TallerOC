anio_actual = 2025
try:
    anio_texto=input("¿En que año naciste?")
    anio_numero=int(anio_texto)
    edad_actual=anio_actual-anio_numero
    if edad_actual>18:
        print("Sos mayor de edad, puedes pasar")
    elif edad_actual<18:
        print("Sos menor de edad, no puedes pasar")
    else:
        print("Sos mayor de edad, puedes pasar")
except ValueError:
    print("Ingrese un año valido en numero")