# programa que muestre si eres mayor de edad

def mayor(e):
    if e>=18:
        print("eres mayor de edad")
    else:
        print("eres menor de edad")

valor= int(input("Escribe tu edad"))
mayor(valor)