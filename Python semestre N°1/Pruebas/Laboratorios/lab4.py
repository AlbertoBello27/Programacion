#Ejercicio 1

trabajadores=[["Juan",[700000,650000,690000]]["Maria",[681000,710000,590000]]["Pedro",[590000,635000,705000]]]

juan=trabajadores[0]
juan_persona=juan[0]
sueldo_juan=juan[1]

maria=trabajadores[1]
maria_persona=maria[0]
sueldo_maria=maria[1]

pedro=trabajadores[2]
pedro_persona=pedro[0]
sueldo_pedro=pedro[1]

#a

def promedio(x):
    promedio1=(sum(x))/len(x)
    promedio2=promedio1.round(promedio1,2)
    return promedio2

#b

def sueldo_alto(x):
    return max(x)

#c

def impuesto(x):
    impuesto=x*0.1225
    return impuesto

prom_juan=promedio(sueldo_juan)
prom_maria=promedio(sueldo_maria)
prom_pedro=promedio(sueldo_pedro)

juan_alto=sueldo_alto(sueldo_juan)
maria_alto=sueldo_alto(sueldo_maria)
pedro_alto=sueldo_alto(sueldo_pedro)

juan_imp=impuesto(juan_alto)
maria_imp=impuesto(maria_alto)
pedro_imp=impuesto(pedro_alto)

lista=[]
for i in range(1):
    lista.append(juan_persona)
    lista.append(prom_juan)
    lista.append(juan_alto)
    lista.append(juan_imp)

lista2=[]
for i in range(1):
    lista2.append(maria_persona)
    lista2.append(prom_maria)
    lista2.append(maria_alto)
    lista2.append(maria_imp)

lista3=[]
for i in range(1):
    lista3.append(pedro_persona)
    lista3.append(prom_pedro)
    lista3.append(pedro_alto)
    lista3.append(pedro_imp)

#Ejercicio 2

a=[10,80,15,30,20]
b=[20,45,80,20,10]
c=[20,35,60,90,20]

def comun(a,b,c):
    set(a)
    set(b)
    set(c)
    d=[]
    d.append(a)
    d.append(b)
    d.append(c)
    set(d)
    print("Los numeros en comun son",d)
    return d

def cont(a,b,c):
    conkat=a+b+c
    print(conkat)
    return

def dup(conkat):
    sin_dups=set(conkat)
    list(sin_dups)
    print(sin_dups)
    return sin_dups

def orden(sin_dups):
    sin_dups.sort(reverse=True)
    print(sin_dups)
    return sin_dups

def añadir(sin_dups):
    sin_dups[6]=100
    print(sin_dups)
    return sin_dups

comun(a,b,c)

comun(a,b,c)
cont(a,b,c)
dup(a,b,c)
orden(a,b,c)
añadir(a,b,c)