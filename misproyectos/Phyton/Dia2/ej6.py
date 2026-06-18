agenda = {
    "santi":"1",
    "benja":"2",
    "dante":"3",
    }
usu=input("Introduce un nombre:")
if usu == "santi":
    print(f"El telefono de santi es {agenda.get('santi')}")
elif usu == "benja":
    print(f"El telefono de benja es {agenda.get('benja')}")
if usu=="dante":
    print(f"El telefono de dante es {agenda.get('dante')}")
