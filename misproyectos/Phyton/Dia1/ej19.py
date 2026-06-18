try:
    numsecreto=3
    num_usuario=input("Decime un numero del 1-10 entero ")
    num_usuario_num=int(num_usuario)
    if numsecreto == num_usuario_num:
        print (f"Ganaste, el numero secreto era: {numsecreto}")
    elif numsecreto  != num_usuario_num:
        print("Intenta de nuevo")
except ValueError:
    print("Ingrese un numero valido")