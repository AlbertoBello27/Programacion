"""UN SIMPLE PRINT"""
print ("Hola")

#UN SIMPLE PRINT 
print ("ola") 
print ("pan con palta")
print ("-")

#DECLARO VARIABLE
name = "Alberto"
nombre = "Ignacio"
x = "Bello"
z= "Soto"
print (name)
print (nombre)
print (x)
print (z)
print("-")
print ("Hola soy", name)
print ("Hola soy", nombre)
print ("Hola soy",name,nombre,x,z)
s = ", me gusta la palta"
print ("Hola soy",name,nombre,x,z,s)

#OTRA VARIABLE (DE TIPO NUMERICA)
edad = 19
print ("Hola tengo",edad)

#MAS COSAS
print ("Hola soy",name)
print ("Hola soy"+name)

#print ("hola mi nombre es"+name,nombre,x,z+"y tengo"+edad)
print ("Hola mi nombre es"+name+nombre+x+z+"y tengo"+str(edad))
print ("Hola mi nombre es",name,nombre,x,z,"y tengo",str(edad))
print ("Hola mi nombre es"+" "+name+" "+nombre+" "+x+" "+z+" ""y tengo"+"")
print ("Hola mi nombre es")

#VARIABLE MUTABLE
name = "Pablo"
print ("Hola mi nuevo nombre es",name)

#OTRA INSTRUCCION
#nombre = input("¿Cual es tu nombre?")
#print("tu nombre es",name,"mentiroso")

nombre = "Alberto"

print (f"Hola mi nombre es {nombre}")

nombre, apellido = "Ignacio" , "Soto"
print(f"Mi nombre es {nombre} {apellido}")