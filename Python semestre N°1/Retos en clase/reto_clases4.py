nombre1=input("Ingrese el nombre del primer paciente: ")
peso1=float(input("Ingrese el peso de la primera persona (en kilogramos): "))
while float(peso1)<3 or float(peso1)>500:
    peso1=input("Ingrese un peso valido: ")
estatura1=float(input("Ingrese la estatura de la primera persona (en metros): "))
while float(estatura1)<0.4 or float(estatura1)>2.7:
    estatura1=input("Ingrese una estatura valida: ")
edad1=int(input("Ingrese la edad de la primera persona: "))
while int(edad1)<0 or int(edad1)>130:
    edad1=input("Ingrese una edad valida: ")
print("")
nombre2=input("Ingrese el nombre del segundo paciente: ")
peso2=float(input("Ingrese el peso de la segunda persona (en kilogramos): "))
while float(peso2)<3 or float(peso2)>500:
    peso2=input("Ingrese un peso valido: ")
estatura2=float(input("Ingrese la estatura de la segunda persona (en metros): "))
while float(estatura2)<0.4 or float(estatura2)>2.7:
    estatura2=input("Ingrese una estatura valida: ")
edad2=int(input("Ingrese la edad de la segunda persona: "))
while int(edad2)<0 or int(edad2)>130:
    edad2=input("Ingrese una edad valida: ")
print("")
nombre3=input("Ingrese el nombre del tercer paciente: ")
peso3=float(input("Ingrese el peso de la tercera persona (en kilogramos): "))
while float(peso3)<3 or float(peso3)>500:
    peso3=input("Ingrese un peso valido: ")
estatura3=float(input("Ingrese la estatura de la tercera persona (en metros): "))
while float(estatura3)<0.4 or float(estatura3)>2.7:
    estatura3=input("Ingrese una estatura valida: ")
edad3=int(input("Ingrese la edad de la tercera persona: "))
print("")
while int(edad3)<0 or int(edad3)>130:
    edad3=input("Ingrese una edad valida: ")
paciente1=(nombre1,peso1,estatura1,edad1)
paciente2=(nombre2,peso2,estatura2,edad2)
paciente3=(nombre3,peso3,estatura3,edad3)
pacientes=[paciente1,paciente2,paciente3]
print(pacientes)