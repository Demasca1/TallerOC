decisionpro="piedra"
decisionusu=input("Decide entre piedra, papel o tijera para jugar: ")
if decisionpro == decisionusu:
    print("Has empatado con el programa")
elif decisionusu == "papel":
    print("Has ganado, felicidades")
else:
    print("Has perdido, que pena")