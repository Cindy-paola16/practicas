#hacer un programa que lea nombre edad y sexo de 10 personas, el programa mostrara
#cuantos hombres mayores de edad,menores, y mujeres mayores y menores hay.
#b=int(input("ingrese su edad"))
#c=input("ingrese su sexo, m o f")


cmm= 0
cmf= 0
cmf= 0
cmm= 0
for i in range(10):
 a=input("ingrese su nombre: ")
 b=int(input("ingrese su edad: "))
 c=input ("ingrese su sexo, m o f :" )
 if b >= 18 and c=='m':
    cMM+=1
 if b<18 and c=='m':
    cmm+=1
 if b >= 18 and c=='f':
    cMF+=1
 if b<18 and c=='f':
    cmf+=1

print("La cantidad de hombres mayores es de :",cmm," ","Y la cantidad de hombres menores es de :",cmm)
print("La cantidad de Mujeres mayores es de :",cmf," ","Y la cantidad de mujeres menores es de :",cmf)    
