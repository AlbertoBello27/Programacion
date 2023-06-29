#01-FUNCIONES SIMPLES
def mi_no_primera_funcion():
    print("Esta no es mi primera funcion")

mi_no_primera_funcion()

def concatenar(lista1,lista2): #Scope global
    return lista1+lista2 #Scope local

lista1=[1,2,3]
lista2=[4,5,6]

print(concatenar(lista1,lista2))
#02-DECLARANDO UNA FUNCION MULTIPLE

def multiplicacion(num1,num2):
    return num1*num2

print(multiplicacion(50,50))
print(multiplicacion(5,5))

def resta(a,b):
    return a-b

a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))

resultado1=resta(a,b)
print(resultado1)

def suma(a,b):
    return a+b

resultado2=suma(a,b)
print(resultado2)
#len(), count(), sort() => FUNCIONES PROPIAS DE PYTHON