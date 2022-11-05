#Problema 3

#Generar un programa que reciba dos cadenas de texto y retorne
#la mayor cadena subsecuente (que sea subsecuente no quiere
#decir que tiene que ser obligatoriamente continua) (ej. fsnutno -
#tsmunio , cadena subsecuente: suo).

import os

print('..::Hackaton - Cadenas subsecuentes - 2022:..')

while True:
    cadena1 = input('Ingrese la primera cadena de texto: ')
    cadena2 = input('Ingrese la segunda cadena de texto: ')
    print('Cadena 1: ', cadena1 + '\nCadena 2: ', cadena2)
    cadena1_array = list(cadena1)
    cadena2_array = list(cadena2)
    max_cadena = len(cadena1_array) if len(cadena1_array) > len(cadena2_array) else len(cadena2_array)
    subsecuentes = ""
    for i in range(max_cadena):
        if cadena1[i] == cadena2[i]:
            subsecuentes += cadena1[i]

    if subsecuentes == "":
        print('..::No hay cadenas subsecuentes:..')
    else:
        print('\x1b[6;30;42m' + 'Cadena subsecuentes: ', subsecuentes + '\x1b[0m')