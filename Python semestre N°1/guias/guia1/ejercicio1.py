texto= "La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion democratica."
texto=texto.split()
contador=0
lista=[]
for i in texto:
    if i=="universidad" or i=="Universidad":
        contador+=1
        lista.append(i)
print(f"La palabra universidad se repite {contador} veces")
print(tuple(lista))