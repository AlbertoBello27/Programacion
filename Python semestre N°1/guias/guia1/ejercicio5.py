import random
"""Crear 20 numeros, que se encuentren en el intervarlo 40 al 350 y los almacene en una
lista y luego pida buscar algun numero dentro de los almacenados. Ademas que muestre
la cantidad de ocurrencias de ese numero buscado"""
lista=[]

for i in range(20):
    a=random.randint(40,351)
    lista.append(a)

print(lista)

b=int(input("Ingrese el numero a buscar\n"))

for j in lista:
    if j!=b:
        print("Numero no encontrado")
        break
    elif j==b:
        c=lista.count(b)
        print("Numero encontrado",c)
        break