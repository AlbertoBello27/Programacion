nombre=input("Escriba el nombre del estudiante:")
asignatura=input("Escriba el nombre de la asignatura:")
nota_lab1=input("Ingrese la primera nota del laboratorio:")
nota_lab2=input("Ingrese la segunda nota del laboratorio:")

operacion=float(nota_lab1)*0.3+float(nota_lab2)*0.7
resultado=(f"{operacion:.1f}")

diccionario={
"Nombre": str(nombre),
"Asignatura": str(asignatura),
"Nota laboratorio N°1": float(nota_lab1),
"Nota laboratorio N°2": float(nota_lab2),
"Nota final":resultado
}
print(diccionario)