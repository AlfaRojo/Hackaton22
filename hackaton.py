import os

print('..::Hackaton 2022:..')
print('..::Bienvenido:..')
print('..::Por favor ingrese una opción..')
print('1. Scramble')
print('2. Justificador de texto')
print('3. Cadenas subsecuentes')
print('4. Abuela binaria')
print('5. Salir')

while True:
    opcion = input('Ingrese una opción: ')
    if opcion == '1':
        print('..::Scramble:..')
        os.system('python ./scramble.py')
        break
    elif opcion == '2':
        print('..::Justificador de texto:..')
        os.system('python justificador.py')
        break
    elif opcion == '3':
        print('..::Cadenas subsecuentes:..')
        os.system('python subsecuencias.py')
        break
    elif opcion == '4':
        print('..::Abuela binaria:..')
        os.system('python abuela.py')
        break
    elif opcion == '5':
        print('..::Saliendo:..')
        break
    else:
        print('..::Opción no válida:..')