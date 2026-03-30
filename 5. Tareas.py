# Ejercicio 1

'''
nota1 = float(input(f'Ingrese la primera calificacion -> '))
nota2 = float(input(f'Ingrese la segunda calificacion -> '))
nota3 = float(input(f'Ingrese la tercera calificacion -> '))
nota4 = float(input(f'Ingrese la cuarta calificacion -> '))

notas = (6.0, 10.0)
notas_total = [nota1, nota2, nota3, nota4]



'''
'''
# Ejercicio 2
tupla = ('admin', 'root', 'sex', 'porn')
usuario = input(f'Proponga un nombre de usuario -> ').lower()

intentos = []

while usuario in tupla:
    print('El nombre esta bloqueado')
    intentos.append(usuario)
    input(f'Proponga un nombre de usuario -> ')
print()

        '''



'''

for n in range(5):
    if notas_total >= notas:
        print(f'Es aprobatoria')

'''



'''

# Ejercicio 2

prohibidos = ('admin', 'root', 'usuario', 'contrase', 'sex')

intentos = []

nombres = input(f'Crea tu nombre de usuario: ').lower()

while nombres in prohibidos:
    print("Ese nombre esta bloqueado ")
    intentos.append(nombres)

    nombres = input(f'Elige otro nombre: ').lower()

print('Valido')
print(f'intentos fallidos, {intentos}')
'''


   
# Ejercicio 3

    presupuesto = float(input('Ingrese su presupuesto -> '))

    canasta = []

    tupla = [
        ('Laptop 150$', 150), 
        ('Nevera 500$', 500), 
        ('Telefono 99.99$', 99.99), 
        ('Audifono 49.99$', 49.99), 
        ('Teclado 15.50$', 15.50)
    ]

    for t in tupla:
        if presupuesto>=t[1]:
            print(t[0])
            canasta.append(t[0])
    input('Ingrese lo que quiere comprar -> ')

        
        