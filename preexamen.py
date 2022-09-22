
n = 1
par = impar = 0
while n != 0:
   n = int(input("ingrese un numero: "))
   if n > 0:
    if n % 2== 0:
        par += 1
    else:
            impar += 1
            print("El total de numeros pares es: " ,par)
            print("El total de numeros impares es: " ,impar)

