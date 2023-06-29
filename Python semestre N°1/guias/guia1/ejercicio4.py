n=int(input("Ingrese el cubo que quiere ejecutar: "))
while n<1:
    n=int(input("Ingrese un numero de cubos valido porn favor: "))

lista=[]
aux=1
aux2=2
for i in range(n-1):
    aux=aux+aux2
    aux2+=1
var=1
for i in range(aux):
    lista.append(var)
    var+=2
lista=lista[aux-n:]
print(f"Los elementos que se usaran para crear el cubo son: {lista}")
lista=sum(lista)
print(f"El cubo del numero {n} es: {lista}")