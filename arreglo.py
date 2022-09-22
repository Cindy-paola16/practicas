from io import UnsupportedOperation


def llenar(x):
    a = int(input('Escribe un numero'))
    arr.append(a)
    x += 1
    if x < 5:
        llenar(x)

def mostrar():
    for x in range(0,len(arr)):
        print(x," ",arr[x],"\n")

        def pila():
            for x range(0,len(arr)):
                arr.pop(aux)
                mostrar()
                aux -=1

def liberarArreglo():
    valor = int(input('Escribe la posicion a eliminar'))
    if valor>=0 and valor<len(arr):
        arr.pop(valor)
    else:
        print('Posicion incorrecta')

x = 0
arr = []
res = "si"
llenar(x)
mostrar()
while(res=="si"):
    liberarArreglo()
    mostrar()
    res = input('Deseas otro ejecusion si/no')


    hacer un programa que mueste el siguiente menu llenar pila, cola , el programa 
    1 si el arreglo esta vacio no se puede elegir la opcion 2 y la opcion 3
    2 una vez llenado el arreglo no se puede elegir la opcion 1 y el programa no termina asta que el usuario lo dese
    