Ciudades=["Santiago", "Temuco","Osorno", "Punta Arenas"]
Indice_calidad_aire=[134,99,245,50]
Ciudades=["Santiago", "Temuco","Osorno", "Punta Arenas"]
Indice_calidad_aire=[134,99,245,50]
minimo=Indice_calidad_aire.index(min(Indice_calidad_aire))
print(f"La ciudad con el indice mas bajo es {Ciudades[minimo]} con un indice de {Indice_calidad_aire[minimo]} Indice de calidad de aire")
maximo=Indice_calidad_aire.index(max(Indice_calidad_aire))
print(f"La ciudad con el indice mas alto es {Ciudades[maximo]} con un indice de {Indice_calidad_aire[maximo]} Indice de calidad de aire")
print("")
for i in range(len(Ciudades)):
    if Indice_calidad_aire[i]>=0 and Indice_calidad_aire[i]<=50:
        print(Ciudades[i],"tiene una calidad de aire buena")
    elif Indice_calidad_aire[i]>=51 and Indice_calidad_aire[i]<=100:
         print(Ciudades[i],"tiene una calidad de aire moderada")
    elif Indice_calidad_aire[i]>=101 and Indice_calidad_aire[i]<=150:
         print(Ciudades[i],"tiene una calidad de aire que puede dañar a grupos sensibles")
    elif Indice_calidad_aire[i]>=151 and Indice_calidad_aire[i]<=200:
         print(Ciudades[i],"tiene una calidad de aire que es dañina para la salud")
    elif Indice_calidad_aire[i]>=201 and Indice_calidad_aire[i]<=300:
         print(Ciudades[i],"tiene una calidad de aire muy dañina para la salud")
    else:
         print(Ciudades[i],"tiene una calidad de aire peligrosa para la salud")