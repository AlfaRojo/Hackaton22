#Problema 2

#Generar un programa que reciba un array de strings y una
#cantidad máxima de caracteres por línea. El programa debe
#justificar cada línea, dejando la cantidad máxima en cada una y
#rellenando los espacios con ' ' de ser necesario para que todo
#quede justificado. Además, la última línea deberá quedar
#justificada a la izquierda sin espacios extra entre palabras.

import os

print('..::Hackaton - Justificador de texto - 2022:..')

while True:
    cadena = input('Ingrese el texto a justificar: ')
    maximo = int(input('Ingrese la cantidad máxima de caracteres por línea: '))
    cadena_array = cadena.split(' ')
    cadena_array_justificada = []
    cadena_array_justificada.append(cadena_array[0])
    cadena_array_justificada.append(' ')
    for i in range(1, len(cadena_array)):
        if len(cadena_array_justificada[-1]) + len(cadena_array[i]) + 1 <= maximo:
            cadena_array_justificada.append(cadena_array[i])
        else:
            cadena_array_justificada.append(cadena_array[i])
    
    for i in range(0, len(cadena_array_justificada)):
        if len(cadena_array_justificada[i]) < maximo:
            cadena_array_justificada[i] = cadena_array_justificada[i] + ' ' * (maximo - len(cadena_array_justificada[i]))
            cadena_array_justificada[i] = cadena_array_justificada[i].ljust(maximo)
            print("\"" + cadena_array_justificada[i] + "\"")
    