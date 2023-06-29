#01-CONDICIONALES

licencia=False
edad=19
auto=False

if licencia:
    print("Puedo conducir porque tengo licencia")
else:
    print("No tengo licencia para conducir")
print("Este print esta fuera del else")

if edad:
    print("Puedo conducir porque soy mayor de edad")
else:
    print("No puedo conducir soy menor de edad")

if edad >= 18:
    print("Puedo conducir porque soy mayor de edad")
else:
    print("No puedo conducir soy menor de edad")

if licencia and edad >= 18:
    print("Puedo conducir porque soy mayor de edad y tengo licencia")
elif auto:
    print("Tengo automovil, pero no tengo licencia ni la edad necesaria")
else:
    print("No puedo conducir no tengo ni la edad, ni licencia ni automovil")