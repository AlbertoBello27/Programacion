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