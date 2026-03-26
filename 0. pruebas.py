


'''
for i in range (1, 11):

    if i % 2 == 0:
        print(f'{i} es un numero par')

        break
        print('hola ese es tu numero par')

    else:

        print(f'{i} es un numero impar')
        '''



'''''
contador = 0
while contador < 100:
    contador += 1

    if contador % 2 == 0:
        continue

    print(f'Contador impar: {contador}')

    if contador >= 100:
        break

'''
nombres = ['Alice', 'Bob', 'Charlie', 'David', 'EvE']

anidacion = [
         ['Alice', 50, 1.00],
         ['Bod', 75.5, 1.75],
         ['Charlie', 10, 1,65],
         ['David', 18, 1.70],
         ['Eve', 20, 1.60]
]

print(f'Lista de nombres: {nombres[0]}')
print(f'Lista de nombres: {nombres[0]}')

#modificar

nombres[2] = 'Messi'
print(f'Nombres de modificacion {nombres}')

#agregar

nombres.append('frank')
print(f'Nuevo nombre: {nombres}')

#insertar reemplazar
nombres.insert('Nancy')
print(f'nombres despues de insertar un nombre: {nombres}')


