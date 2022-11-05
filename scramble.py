#Problema 1

#Generar un programa que reciba dos cadenas de texto de la
#misma longitud y retorne un valor booleano indicando si la
#segunda cadena es una cadena desordenada de la primera
#cadena (ej. Deudora - Eduardo TRUE, Fresa - Uva FALSE).

import os

print('..::Hackaton - Scramble - 2022:..')

while True:
    cadena1 = input('Ingrese la primera cadena de texto: ')
    cadena2 = input('Ingrese la segunda cadena de texto: ')
    if len(cadena1) != len(cadena2):
        print('..::Las cadenas no tienen la misma longitud:..')
    else:
        print('Cadena 1: ', cadena1 + '\nCadena 2: ', cadena2)
        cadena1_array = list(cadena1)
        cadena2_array = list(cadena2)
        cadena1_array.sort()
        cadena2_array.sort()
        if cadena1_array == cadena2_array:
            print('\x1b[6;30;42m' + '==> La segunda cadena es una cadena desordenada de la primera cadena.' + '\x1b[0m' + '\n\n')
        else:
            print('\x1b[0;31;40m' + '==> La segunda cadena no es una cadena desordenada de la primera cadena.' + '\x1b[0m' + '\n\n')
        break