from curses.ascii import isdigit


def validarletras(a):
    for i in a:
     if a.isdigit(i):  
        print("Es una letra")
     else:
         print("No es caracte")    #analiza cada digito y si no es alfanumerico retorna a falso

a= input("Escribe un nombre")
validarletras(a)

'