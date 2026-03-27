# Ejercicio 1

num = int(input("Ingrese el primer numero: "))
if num % 2 == 0:
    print(f"El numero {num} es par")
else:    print(f"El numero {num} es impar")


# Ejercicio 2
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:
    print(f"El numero {num1} es mayor que {num2}")    

elif num2 > num1:
    print(f"El numero {num2} es mayor que {num1}")

elif num1 == num2:
    print(f"Los numeros {num1} y {num2} son iguales")

else:
        print("Error, ingrese un numero valido")  

# Ejercicio 3

edad10 = int(input("Ingrese la edad: "))

if edad10 >= 18:
      print(f'Tienes {edad10} eres mayor de edad')
else:
      print(f'Tienes {edad10} No eres mayor de edad')



# Ejercicio 4
compra = float(input(f'Ingrese el monto final de su compra: '))
descuento = compra * 0.15
precio_final = compra - descuento

if compra > 1000:
    print(f'Ha recibido un descuento de 15%, paga en total: {precio_final}')
else:
    print(f'Usted ha pagado el precio regular: {compra}')


# Ejercicio 5
año = int(input('Ingrese un año: '))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print('Es un año bisiesto')
else:
    print('No es un año bisiesto')


# Ejercicio 6

nm = float(input('Ingrese su primer numero a operar: '))
nm1 = float(input('Ingrese su segundo numero a operar: '))

suma = nm + nm1
resta = nm - nm1
multiplica = nm * nm1
divisi = nm / nm1


operador = input("Ingresa el operador: ").strip()

if operador == '+':
    print(f'Su suma es: {suma} ')
elif operador == '-':
    print(f'Su resta es: {resta} ')
elif operador == '*':
    print(f'Su multiplicacion es: {multiplica} ')
elif operador == '/':
    if nm1 == 0:
        print('No se puede dividir sobre cero')
    else:
        print(f'Su division es: {divisi}')

# Ejercicio 7

triangulo = int(input(f'Primer lado del triangulo: '))
triangulo1 = int(input(f'Segundo lado del triangulo: '))
triangulo2 = int(input(f'Tercero lado del triangulo: '))


if triangulo + triangulo1 > triangulo2 and triangulo + triangulo2 > triangulo1 and triangulo1 + triangulo2 > triangulo:

    if triangulo == triangulo1 == triangulo2:
        print('El triangulo es equilatero')

    elif triangulo == triangulo1 or triangulo == triangulo2 or triangulo1 == triangulo2:
        print('El triangulo es isosceles')

    else:
        print('El triangulo es escaleno')
else:
    print('No es un triangulo valido')


# Ejercicio 8

calificacion = int(input('Ingrese su calificacion: '))

if calificacion >= 90 and calificacion <= 100:
    print('A')
elif calificacion >= 80 and calificacion <= 89:
        print('b')
elif calificacion >= 70 and calificacion <= 79:
            print('C')
elif calificacion >= 60 and calificacion <= 69:
                print('D')
elif calificacion >= 0 and calificacion <=59:
                    print('F')
else:
    print('Error, no opcion valida')       
     



#Ejercicio 9
print("\nBienvenido al programa de becas universitarias.")

promedio = float(input("Ingrese la primera nota del estudiante: "))
ingresos = float(input("Ingrese los ingresos mensuales del estudiante: "))
reportes_disciplinarios = bool(input("¿El estudiante tiene reportes disciplinarios? (true/false): ").lower())

if (promedio >= 8.5 and ingresos < 2000) and not reportes_disciplinarios:
    print("\nEl estudiante es elegible para la beca.")

else:
    print("\nEl estudiante no es elegible para la beca.")


# Ejercicio 10

jugador = input(f'Que movimiento eligira el primer participante PIEDRA, PAPEL o TIJERA >').strip()
jugador1 = input(f'Que movimiento eligiras el segundo participante PIEDRA, PAPEL o TIJERA >').strip()

if jugador ==  jugador1:
     print('Empate')

elif jugador == 'piedra' and jugador1 == 'tijera':
     print(f'{jugador} Ha ganado el primer')
elif jugador =='tijera' and jugador1 == 'papel':
     print(f'{jugador} Ha ganado el primer')
elif jugador == 'papel' and jugador1 == 'piedra':
     print(f'{jugador} Ha ganado el primer')
else:
     print(f'{jugador1} Ha ganado el segundo')

     