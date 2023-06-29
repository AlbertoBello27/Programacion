tarifa_diurna=12000
tarifa_nocturna=16000
inc_diurno_dom=2000
inc_nocturno_dom=3000

def reset(Dias):
    Dias["lunes"]=0
    Dias["martes"]=0
    Dias["miecoles"]=0
    Dias["jueves"]=0
    Dias["viernes"]=0

Dias={
    "lunes":0,
    "martes":0,
    "miecoles":0,
    "jueves":0,
    "viernes":0,
    "sabado":0,
    "domingo":0
}

emplpeado1={
    "Nombre":"Empleado I",
    "Pago Diario":Dias,
    "Pago Semanal":0,
}

Dias["lunes"]=int(tarifa_nocturna*10)
Dias["martes"]=int(tarifa_nocturna*10)
Dias["miecoles"]=int(tarifa_nocturna*10)
Dias["jueves"]=int(tarifa_diurna*10)
Dias["viernes"]=int(tarifa_diurna*10)
emplpeado1["Pago Semanal"]=sum(Dias.values())
print(emplpeado1)
reset(Dias)

emplpeado2={
    "Nombre":"Empleado II",
    "Pago Diario":Dias,
    "Pago Semanal":0,
}

Dias["martes"]=int(tarifa_nocturna*10)
Dias["miecoles"]=int(tarifa_nocturna*10)
Dias["jueves"]=int(tarifa_nocturna*10)
Dias["domingo"]=int((tarifa_diurna+inc_diurno_dom)*10)
emplpeado2["Pago Semanal"]=sum(Dias.values())
print(emplpeado2)
reset(Dias)

emplpeado3={
    "Nombre":"Empleado III",
    "Pago Diario":Dias,
    "Pago Semanal":0,
}

Dias["miecoles"]=int(tarifa_diurna*10)
Dias["jueves"]=int(tarifa_diurna*10)
Dias["viernes"]=int(tarifa_diurna*10)
Dias["sabado"]=int(tarifa_nocturna*10)
Dias["domingo"]=int((tarifa_nocturna+inc_nocturno_dom)*10)
emplpeado3["Pago Semanal"]=sum(Dias.values())
print(emplpeado3)