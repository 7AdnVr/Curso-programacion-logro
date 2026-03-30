
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
    
        print("Opcion no valida")
     

    usuario = int(input("Vuelva elegir el numero -> "))


print("Ha adinivado el numero")


# Ejercicio 3

usuario10 = input("Ingrese un numero o fin si quiere terminar ->   ").lower()

lista = []

while usuario10 != "fin":
    
    if usuario10 >= 0:
        suma = input('Que numero desea poner -> ')
        lista.append(suma)
    
    usuario10 = int(input("Ingrese un numero o ""fin"" si quiere terminar ->")).lower()

print("Ha terminado el programa")
print(f"Este es el promedio de los numero ingresados {lista[0]}")

# Ejercicio 4

me = input(f"Escriba un palindromo -> ").strip()




# Ejercicio 6

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

suma = 0

for n in numeros:

    if n % 2 == 0:
        suma += n

print(f"La suma de los numeros pares es: {suma}")