###Programa que simula el comportamiento de un relog y se detiene a las 23:59:59###
for hrs in range(24):
    for min in range(60):
        for seg in range(60):
            print(f"{hrs:02}:{min:02}:{seg:02}")
            if hrs==23 and min==59 and seg==59:
                print("Fin del Programa")
                break