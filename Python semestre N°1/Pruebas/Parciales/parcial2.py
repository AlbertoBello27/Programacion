#Ejercicio_1
palabra=input("Ingrese una palabra: ")
lista=list(palabra)
lista2=[]
cont=-1
for i in range(len(lista)):
    lista2.append(lista[cont])
    cont-=1
if lista==lista2:
    print("Es palindromo")
else:
    print("No es palindromo")
    
#Ejercicio_2
for i in range(1,11):
    if i==1:
        print(i)
    elif i==2:
        print(i,i+1,i,sep="")
    elif i==3:
        print(i,i+1,i+2,i+1,i,sep="")
    elif i==4:
        print(i,i+1,i+2,i+1,i,sep="")
    elif i==5:
        print(i,i+1,i+2,i+3,i+2,i+1,i,sep="")
    elif i==6:
        print(i,i+1,i+2,i+3,i+4,i+3,i+2,i+1,i,sep="")
    elif i==7:
        print(i,i+1,i+2,i+3,i+4,i+5,i+4,i+3,i+2,i+1,i,sep="")
    elif i==8:
        print(i,i+1,i+2,i+3,i+4,i+5,i+6,i+5,i+4,i+3,i+2,i+1,i,sep="")
    elif i==9:
        print(i,i+1,i+2,i+3,i+4,i+5,i+6,i+7,i+6,i+5,i+4,i+3,i+2,i+1,i,sep="")
    elif i==10:
        print(i,i+1,i+2,i+3,i+4,i+5,i+6,i+7,i+8,i+7,i+5,i+4,i+3,i+2,i+1,i,sep="")
#Ejercicio_3
temp_min={9,5,2,7,6,1}
temp_max={12,14,11,10,15,9}
#a
print(f"El elemento que se encuentra en ambos sets son: {temp_min.intersection(temp_max)}")
#b
en_temp_min_6=6 in temp_min
if en_temp_min_6==True:
    en_temp_min_6="Verdadero"
en_temp_max_6=6 in temp_max
if en_temp_max_6!=True:
    en_temp_max_6="Falso"
en_temp_min_17=17 in temp_min
if en_temp_min_17!=True:
    en_temp_min_17="Falso"
en_temp_max_17=17 in temp_max
if en_temp_max_17!=True:
    en_temp_max_17="Falso"
print(f"El 6 aparece en el primer set: {en_temp_min_6}, en el segundo: {en_temp_max_6}, el 17 aparece en el primer set: {en_temp_min_17}, en el segundo: {en_temp_max_17}")
#c
lista1=list(temp_min)
lista_elevada1=[]
for i in lista1:
    var=i**4
    lista_elevada1.append(var)
set_elevado1=set(lista_elevada1)
print(f"El primer set elevado queda asi: {set_elevado1}")

lista2=list(temp_max)
lista_elevada2=[]
for i in lista2:
    var=i**4
    lista_elevada2.append(var)
set_elevado2=set(lista_elevada2)
print(f"El segundo set elevado queda asi: {set_elevado2}")
#d
set_final=set(lista_elevada1+lista_elevada2)
print(f"Los dos set combinados quedan asi: {set_final}")