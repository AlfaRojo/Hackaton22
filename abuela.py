#Problema 4

#Generar un programa que reciba tres números, N que será el
#total y dos números que sumados den como resultado N. La
#abuela le regalará a su nieta la cantidad de avellanas de la suma
#de la cantidad de unos de los dos números en binario. ( ej. El
#total es 7, y los dos números son 3 (11) y 4 (100), en ese caso la
#abuela le dará a su nieta 3 avellanas ).

import os

print('..::Hackaton - Abuela - 2022:..')

while True:
    total = int(input('Ingrese el total de avellanas: '))
    numero1 = int(input('Ingrese el primer número: '))
    numero2 = int(input('Ingrese el segundo número: '))
    if total < 1:
        print('..::El total de avellanas debe ser mayor a 0:..')
    elif numero1 < 1:
        print('..::El primer número debe ser mayor a 0:..')
    elif numero2 < 1:
        print('..::El segundo número debe ser mayor a 0:..')
    else:
        print('Total de avellanas: ',  total, '\nPrimer número: ', numero1, '\nSegundo número: ', numero2)
        numero1_binario = bin(numero1)
        numero2_binario = bin(numero2)
        print('Número 1 en binario: ', numero1_binario, '\nNúmero 2 en binario: ', numero2_binario)
        numero1_binario_array = list(numero1_binario)
        numero2_binario_array = list(numero2_binario)
        numero1_unos = 0
        numero2_unos = 0
        for i in range(len(numero1_binario_array)):
            if numero1_binario_array[i] == '1':
                numero1_unos += 1
        for i in range(len(numero2_binario_array)):
            if numero2_binario_array[i] == '1':
                numero2_unos += 1
        print('Número 1 en binario con unos: ', numero1_unos, '\nNúmero 2 en binario con unos: ', numero2_unos)
        suma_unos = numero1_unos + numero2_unos
        print('Suma de unos: ', suma_unos)
        if suma_unos > total:
            print('..::La suma de unos es mayor al total de avellanas:..')
        else:
            print('La abuela le dará a su nieta ', suma_unos, ' avellanas')