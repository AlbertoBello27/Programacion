# 4. Disenar un algoritmo que pueda actuar como un cajero, que devuelve y desglosa el vuelto
# en billetes y monedas (pesos chilenos). Utilizando funciones en Python

#=#=#=#=#=#=#=#=#=    INICIO    =#=#=#=#=#=#=#=#=#

def ask_amount():
    while True:
        try:
            amount = int(input('Ingresa el monto a retirar: '))
            if amount < 10:
                print('Ingresa un monto igual o mayor a $10.')
                continue
            elif amount % 10 != 0:
                print('Ingresa un monto multiplo de 10.')
                continue
            else:
                break
        except:
            print('Ingresa un numero valido.')
    return amount

def bills_and_coins(amount):
    bills = [20000, 10000, 5000, 2000, 1000]
    coins = [500, 100, 50, 10]
    reg = {}

    if amount > 990:
        for i in bills:
            if amount // i > 0:
                reg[i] = amount // i
                amount -= i * reg[i]

    if amount <= 990:
        for i in coins:
            if amount // i > 0:
                reg[i] = amount // i
                amount -= i * reg[i]
    return reg

def show_screen():
    amount = ask_amount()
    print('\nDesglose:\n')
    for k, v in bills_and_coins(amount).items():
        print('➼  $', k, ' x ', v, sep='')


print('\n##### EJERCICIO 02 #####\n')
show_screen()
print('\n##### FIN EJERCICIO #####\n')

#=#=#=#=#=#=#=#=#=#=    FIN    #=#=#=#=#=#=#=#=#=#=#