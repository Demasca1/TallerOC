try:
    total_text=input("Total de la cuenta:")
    total_num=float(total_text)
    prop_text=input("Porcentaje que quieras dejar:")
    prop_porc=int(prop_text)
    prop_total=total_num/prop_porc
    cuenta_tot=total_num+prop_total
    print(f"Monto de la propina: {prop_total}")
    print(f"Tenes que abonar en total {cuenta_tot}")
except ValueError:
    print("Ingrese un porcentaje o total en numero")