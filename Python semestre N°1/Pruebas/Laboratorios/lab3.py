## Ejercicio 1 ##

#a
diccionario={
    "ID":{14,12},
    "Nombre":{"Los Rios","Magallanes"},
    "Superficie(Km2)":{18429,1382291},
    "Habitantes": {404432,166533}
}
print(diccionario)
print()
#b
densidad1=404432/18429
densidad2=166533/1382291
diccionario["Densidad"]=(round(densidad1,1),round(densidad2,1))
#c
diccionario["Capital"]="Valdivia","Punto Arenas"
#d
comunas1="Rio Bueno","La Union","Pallaco"
comunas2="Cabo de Hornos","Puerto Williams","Porvenir"
diccionario["Comunas"]=[comunas1,comunas2]
#e
provincia=("Ranco","valdivia","Antartica Chilena","Magallanes","Tierra del Fuego","Ultima Esperanza")
diccionario["Provincias"]=provincia
#f
print(diccionario)
print()

## Ejercicio 2 ##

a=[21,8,15,3,12]
b=[10,9,12,15,18]
c=[2,3,8,9,12]
#a
juntas=a+b+c
print(juntas)
print()
#b
juntas.insert(-1,20)
print(juntas)
print()
#c
juntas.sort()
juntas2=[]
var=-1
for i in range(len(juntas)):
    juntas2.append(juntas[var])
    var-=1
print(juntas2)
print()
#d
d=[4,5,6]
juntas2.append(sum(d))
print(juntas2)
print()
#e
suma=sum(juntas2)
print(suma)
print()
#f
promedio=suma/len(juntas2)
print(promedio)