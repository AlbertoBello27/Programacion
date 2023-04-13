edad = 19 #ENTERO
estatura = 1.71 #REAL
peso = 60
complejo = 1 +4j #COMPLEJO

print(f"Hola tengo {edad}, mido {estatura} y peso {peso}")

#TRANSFORMAR UN REAL A UN ENTERO
print("Transformando real a entero:",int(peso))

#TRANSFORMAR UN ENTERO A UN REAL
print ("Entero a real:",float(edad))

imc = peso /(estatura**2)
print ("Mi IMC es:",imc)

print("Mi IMC es de {:.5f}" .format(imc))
print("Mi IMC es de {:.1f}" .format(imc))

#DATOS DE TIPO CADENA DE TEXTO (STRING)
asignatura = "Programación"
carrera = "Ingerniería Civil en Informática"
print(f"La asignatura de {asignatura} corresponde a la carrera de {carrera}")

#1: str() = cadena de caracteres
#2: int() = numeros enteros
#3: float() = numero decimales 
#4: len() = cantidad de elementos en la lista
#5: type() = tipo de dato
#6: count() = Determina la cantidad de ocurrencia de un mimso elemento

print(type(carrera))

#LISTAS (ARREGLOS:CONJUNTO DE DATOS DE UN SOLO TIPO)(TAMBIEN PUEDEN SER DE DISTINTOS TIPOS)

array = [0, 1, 2, 3] #ARREGLO
array1 = [0,"algo", "true",1] #LISTA

nueva_lista =list() 
print("Esta es una lista vacia:", nueva_lista)

otra_lista = []
print("Otra lista:", otra_lista)
print(type(otra_lista))

#DECLARANDO OTRAS LISTAS

estudiantes = ["Alberto", "Ignacio", "Jose"]
num = [1,2,3,4,5]
lenguaje = ["python"]

Verdadero = True

cosas = ["casa",7,1.71,1+4j,"palta",True]
print(cosas)

print(len(num))
print(len(cosas))
print(len(lenguaje))

numeros = [1,1,2,2,3,4,5]
print(numeros.count(1))
estudiantes = ["Alberto", "Jose", "Alberto", "Marco", "Jose", "Tomas" , "Jose"]
print(estudiantes.count("Alberto"))
print(estudiantes.count("Jose"))

print(f"Los nuevos estudiantes de {asignatura} de la carrera de {carrera} de este año son {estudiantes}")
print("Los nuevos estudiantes de", asignatura, "de la carerra de", carrera, "de este año son", estudiantes)
print("Los nuevos estudiantes de"+ asignatura + "de la carrera de"+ carrera +"de este año son")

lenguaje = ["JavaScript"]
print(lenguaje)

#INDICE
a = [1,2,3,4,5,777]
print(a[0])
print(a[1])
print(a[2])
print(a[5])

nombres = ["Tomas","Carlos","Matias","Ramiro","Zapallo"]
print(nombres[0])
print(nombres[3])
print(nombres[4])
print(estudiantes[-1])
print(estudiantes[-2])
print(estudiantes[-3])
print(estudiantes[-4])

nombres[1] = "Sopaipilla"
print(nombres[1])
print(nombres)

#OTRA LISTA DE DATOS MIXTOS
cod = 10023
ramo = "Programación"
semestre = 1
estado = True

data_asig = [10023, "Programación",1,True]
cod,ramo,semestre,estado = data_asig
print(ramo)

#SE PUEDEN SUMAR LISTAS
a = [1,2,3,4,5]
b = [10,20,30,40,50]
c = ["carne","papas","nuggets"]
print("Suma de listas", a + b)
print("Suma de listas", a + b + c)

print(list(a))
print(list(range(10))) #CREA UNA LISTA DE RANGO 10
print(list(range(7)))
print(list("JavaScript")) #TRANSFORMA EL STR "JavaScript" EN UNA LISTA

a = 12
print(a+a)
print(float(a+a))

#TRANFORMACIONES NUMERICAS, STRING, LISTAS, INDICES

print(f"hola \n")

print("la variable \"carrera\" es de tipo:", type(carrera))

print("\n") #SALTO DE LINEA

comida = ["carne","papas","peces"]
print(comida)

comida [1] = "papas fritas"
print(comida)

comida [2] = "sushi"
print (comida)

comida[0] = "pollo"
print(comida)

comida[0] = "vaca"