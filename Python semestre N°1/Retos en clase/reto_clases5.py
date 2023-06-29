num=int(input("Ingrese un numero: "))
if num>50:
    print("El numero es mayor que 50")
elif num<50:
    print("El numero es menor que 50")

if num%2==0:
    print("El numero es par")

es_primo="El numero es primo"
for i in range(2, num):
    if num % i == 0:
        es_primo = "El numero no es primo"
        break
    else:
        es_primo="El numero es primo"

print(es_primo)
