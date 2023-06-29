#OTRAS VARIABLES
estatura = 1.71
peso = 70
complejo = 1 + 4j
print("impresion del numero complejo",complejo)

#OPERACION ARITMETICA BASICA
imc = peso/estatura**2
print (imc)
a = 1+1 
print (a)
print (a**2)

#DATOS TIPO CADENA DE CARACTERES (2)
asignatura = "Programacion"
carrera = "Ingeniería civil en Informática"
print ("la asignatura de ",asignatura, "corresponde a la",carrera)

#VALORES BOOLEANOS (3)
ampolleta = False
interruptor = True
#CON TYPE SABEMOS EL TIPO DE DATOS QUE ESTAMOS TRATANDO
print(type(ampolleta))

#DATOS TIPO ARRAY (OBJETOS TIPO COLECCIÓN)(4)
estudiantes = ("Matias","Marco","Cristobal", "Sebastian")
print (estudiantes)
num = [1,2,3,4,5]
print (num)
a = 1+2+3+4+5
print (a)
print (a**2)

#VARIABLES, MATEMATICA BASICA,OTROS TIPOS DE DATOS

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

#05-TUPLAS (NO MUTABLES)
grupo1 = ("Daniel","Cristian","Felipe",200,100,"Daniel")
print(type(grupo1))

#ACCEDIENDO AL PRINMER ELMENTO DE UNA TUPLA
print(grupo1[0])

#CONSULTANDO LA CANTIDAD DE VECES QUE APARECE EL ELEMENTO "Daniel"
print(grupo1.count("Daniel"))

#MUESTRA EL INDICE DEL PRIMER ELMENTO BUSCADO
print("Indice del elemento:",grupo1.index("Daniel"))
print("Indice del elemento:",grupo1.index(200))

#grupo1[0] = "Contanza" #ERROR
#print(grupo1)

grupo2 = ("Pedro","Juan","Diego",777)

print(grupo1 + grupo2)

print(grupo1[2:5])

grupo1 =list(grupo1)
print(type(grupo1))

grupo1[0] = "Constanza"
print(grupo1)

grupo1 = tuple(grupo1)
print(type(grupo1))
grupo1 =list(grupo1)

#06-SETS (CONJUNTOS) (ESTRUCTURA FIJA DE DATOS)
conjunto_lleno = set()
conjunto_lleno1 = {} #¿DICCIONARIO O SET?
print(type(conjunto_lleno))
print(type(conjunto_lleno1))
colores = set({"Rojo","Verde","Azul"})
animales = {"Perro","Gato","Iguana"}
print(type(animales))

#print(animales[0]) NO SE PUEDE

animales.add("Ballena")
print(animales)
animales.add("Mono")
print(animales)

#TUPLAS,INDICE,SETS

#DICCIONARIOS
diccionario={
    "Nombre":"Pepe",
    "Institucion":"Escuela",
    "Edad":4,
    "colores": {"rojo","azul"}
}
print(diccionario)
print(
    "hola "
    "esto es una "
    "prueba"
)
 #ACTUALIZAR VALOR DE UN DICCIONARIO
print(diccionario["Nombre"])
diccionario["Nombre"]= "Alberto"
print(diccionario)

#ELMININANDO CAMPO DE DICCIONARIO
del diccionario["Nombre"]
print(diccionario)

#DICCIONARIOS