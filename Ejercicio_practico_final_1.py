contador = 0
suma = 0
numero = 1

while numero != 0:
    numero = int(input('Ingrese salario (0 para terminar): '))

    if numero != 0:
        suma += numero
        contador += 1

if contador == 0:
    print('No digitó ningún número.')
else:
    promedio = suma / contador

    print('El promedio del salario es igual a {}.'.format(promedio))

if promedio < 300:
    print("Sueldo bajo")
elif promedio > 900:
    print("Sueldo alto")
else:
    print("Sueldo normal")
