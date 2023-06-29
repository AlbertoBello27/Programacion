def ejercicio8():
    separada=frase.split()
    for i in separada:
        diccionario[i]=len(i)
    print(diccionario)
diccionario={}
frase=input("Ingrese una frase: ")

ejercicio8()