#01-WHILE
edad=18
num=0
"""while edad<28:
    print("Eres menor de edad")"""

while num<=100:
    print(num)
    num+=2
else:
    print("Mi condicion es igual o mayor a 100")

#BUCLE INFINITO (USO DE BREAK)
while True:
    parametro=input(">")
    if parametro=="exit":
        break
    else:print(parametro)

#USO DE CONTINUE

num=0
while num<=50:
    num+=1
    if num==40:
        continue
    print(num)

#02-FOR
for i in range(3):
    print("Hello World")

newlista=[1,2,3,4,5,6,7,8,9,10]
for i in newlista:
    print(i)