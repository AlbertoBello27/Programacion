# 5. Desarrollar un programa que permita al usuario ingresar una serie de numeros enteros
# positivos (N numeros) hasta que ingrese -1 (Solo positivos ignorando los numeros negativos). 
# Luego, el programa debe calcular e imprimir en pantalla lo siguiente: el numero
# mayor de los ingresados, la sumatoria total de los numeros, la sumatoria de los numeros
# pares, la sumatoria de los numeros impares y el promedio total. Ademas, se debe imprimir si el numero 
# mayor obtenido es mayor, menor o igual que el promedio calculado.
# Asegurate de resolver este problema utilizando las funciones que consideres adecuadas.

# Nota: el -1 no se cuenta. Si el usuario ingresa un numero negativo debe volver a pedir un
# numero y no se usa en el calculo.

# Ejemplo: el usuario ingresa: 2, 3, 6, 7, 7, 9, -1 se debe imprimir en pantalla:
# La suma de pares es: 8
# La suma de impares es: 26
# La suma total es: 34
# El promedio es: 5
# El numero mayor ingresado fue: 9
# El numero es mayor que el promedio y este es 9

#=#=#=#=#=#=#=#=#=    INICIO    =#=#=#=#=#=#=#=#=#

def ask_nums():
    nums_list = []
    while True:
        try:
            user_num = int(input('Ingresa un numero (o "-1" para salir): '))
            if user_num == -1:
                break
            if user_num < 1:
                print('Ingresa un numero igual o mayor a 1.')
                continue
            else:
                nums_list.append(user_num)
        except:
            print('Ingresa un numero valido.')
    return nums_list

def sum_all_even_odd(num_list):
    sum_even = 0
    sum_odd = 0
    sum_all = sum(num_list)
    for i in num_list:
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    return sum_even, sum_odd, sum_all

sum_zip = sum_all_even_odd(ask_nums())

sum_even = sum_zip[0]
sum_odd = sum_zip[1]
sum_all = sum_zip[2]


print('\n##### EJERCICIO 02 #####\n')

print('La suma de pares es:', sum_even)
print('La suma de impares es:,', sum_odd)
print('La suma total es:', sum_all)

print('\n##### FIN EJERCICIO #####\n')

#=#=#=#=#=#=#=#=#=#=    FIN    #=#=#=#=#=#=#=#=#=#=#