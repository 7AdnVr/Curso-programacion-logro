
import random


frase = input("Ingrese una frase -> ")

h1 = ("a", "e", "i", "o", "u")

vocal = 0
conson = 0

for letra in frase:

    if letra.lower() in h1:
        vocal += 1

    elif letra.lower():
        conson += 1

print(f"tiene {vocal} vocales y {conson} consonantes")

# Ejercicio 2

numero = random.randint(1, 100)

usuario = int(input("Intenta adivinar el numero -> "))

while usuario != numero:

    if usuario > numero:
        print("El numero es muy alto, baja un poco")

    elif usuario < numero:
        print("El numero es muy bajo, sube un poco")
     

    usuario = int(input("Vuelva elegir el numero -> "))


print("Has adinivado el numero")


# Ejercicio 3


lista = [] 

suma = 0

usuario5 = input('Ingrese un numero o ""fin"" si quiere terminar -> ')

while usuario5 != "fin":

    usuario5 = int(usuario5)
    lista.append(usuario5)
    
    usuario5 = input("Ingrese un numero o ""fin"" si quiere terminar -> ")

for m in lista:
    suma = suma + m


print("Ha terminado el programa")
print(f"Este es el promedio de los numero ingresados {suma/len(lista)}")




# Ejercicio 4

print('Agenda de Contactos Simple ')

contactos = {}

while True:
    kj = input('\n1. Añadir\n2. Buscar\n3. Listar\n4. Salir\n-> ')

    if kj == '1':
        nombre = input('Nombre: ')
        numero = input('Numero: ')
        contactos[nombre] = numero

    elif kj == '2':
        nombre = input('Buscar nombre -> ')
        if nombre in contactos:
            print(contactos[nombre])
        else:
            print('No existe el contactop')

    elif kj == '3':
        if not contactos:
            print('No hay contactos')
        else:
            for nombre, numero in contactos.items():
                print(nombre, ":", numero)

    elif kj == '4':
        break

    else:
        print('Opcion invalida')

print('Haz salido correctamente')

# Ejercicio 5





pepe = input('Escriba un parrafo -> ').split()

diccionario20 = {}

for g in pepe:

    if g in diccionario20:
        diccionario20[g] += 1
    else:
        diccionario20[g] = 1
    
print(diccionario20)


# Ejercicio 6

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

suma = 0

for n in numeros:

    if n % 2 == 0:
        suma += n

print(f"La suma de los numeros pares es: {suma}")


# Ejercicio 7


print('Agenda de Contactos Simple 📔')

opciones = (1, 2, 3, 4)

contactos = {}

kj = input('1. Añadir un contacto. \n2. Buscar un contacto. \n3. Listar todos los contactos. \n4. Salir. ')

while kj != '4':

    if kj not in opciones:
        print('\nNinguna opcion es valida\n')

    elif kj == '1':
        ol = input('El nombre y el número de teléfono -> ')
        contactos.update(ol)

    elif kj == '2':



    elif kj == '3':
        if not contactos:
            print('\nNo tienes nada, agrega algo\n')
        else:
            print('\nLista de contactos')
            for i in range(len(contactos)):
                print(f'{contactos}')
            print()
print('Haz salido correctamente')


# Ejercicio 8
lista1 = [1, 2, 5, 6, 'Hola', 'Mundo', 8, 'Futbol']
lista2 = [6, 'Hola', 'Mundo', 8, 9, 0, 'Pepsi']

set1 = set(lista1)
set2 = set(lista2)

tienen = set1.intersection(set2)

print(f'{tienen}')


# Ejercicio 9


list_tuplas = [
    ('nombre', 'Ana'), 
    ('edad', 22), 
    ('ciudad', 'Valencia')
]

diccionario = {}

for clave, valor1 in list_tuplas:
    diccionario[clave] = valor1
    

print(diccionario)




# Ejercicio 10

people = int(input('Ingrese un numero -> '))

multi =  people * '*'

for j in range(people):
    print('*' * people)

