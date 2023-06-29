#OPERADORES ARITMETICOS
a=1
b=3
print("esto es suma: ",a+b)
print("esto es resta: ",a-b)
print("esto es multiplicacion: ",a*b)
print("esto es division: ",a/b)
print("esto es un elevado: ",a**b)

#elevar por un valo que no sea 2
c=2
d=3
print("elevado a 2: ",c**2)
print("elevado a 3: ",c**d)

#CREANDO UN NUMERO COMPLEJO
numeros_complejos=complex(1,2)
print(numeros_complejos)
print(numeros_complejos.real)
print(numeros_complejos.imag)

#MULTIPLICACION Y OTRAS COSAS
print("hola "*10,"adios "*10)
#print("Hola"*3+2) NO SE PUEDE
print("hola "*(int((10+2)/5)))
print("Hola "+str(20))

#OPERADROES DE COMPARACION
q=1
w=2
print(q==w)
print(q!=w)
print(q>w)
print(q<w)
print(q>=w)
print(q<=w)
pez="Salmon"
animal="Tortuga"
print(pez==animal)
print(pez!=animal)
print(pez>animal)
print(pez<animal)
print(len("pez")>len("animal"))

#OPERADORES LOGICOS
bencina=True
encendido=True
edad=19

#UTILIZANDO OPERADOR AND
if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

bencina=False
encendido=False
if not bencina and not encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

bencina=True
encendido=True
if bencina or (encendido and edad >=18):
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")

edad=int(input("Introduce tu edad: "))

if edad<18:
    print("Eres mayor de edad")
elif edad<18:
    print("Eres menor de edad")

#OPERADORES ARITMETICOS, DE COMPARACION, NUMEROS COMPLEJOS, BOOLEANOS, TRUE/FALSE, IF/ELSE