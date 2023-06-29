num=int(input("Ingrese un numero entero: "))
factorial=1
aux=1
for i in range(num):
    factorial=factorial*aux
    aux+=1
    print(f"El factorial de {num} es {factorial}")