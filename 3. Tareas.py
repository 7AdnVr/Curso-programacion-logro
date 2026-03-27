# Ejercicio 1
"""
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

edad1 = int(input("Ingrese la edad de la primera persona: "))
mayor_edad = 18 >=         


"""
# Ejercicio 2
'''
num1 = int(input(f'Cual es su primer numero: '))
num2 = int(input(f'Cual es su segundo numero: '))

if num1 > num2:
   print(f'{num1} Es mayor')

elif num2 > num1:
   print(f'{num2} Es mayor')

else:
    print(f'Los dos son iguales')

# Ejercicio 3 Clasificación de Edad
edad1 = int(input(f'Ingrese su edad > '))

if num1 >= 18:
    print(f'Tienes {edad1}, eres mayor de edad')
else:
 print(f'Tienes {edad1}, eres menor de edad')
'''

'''
# Ejercicio 4
compra = float(input(f'Ingrese el monto final de su compra: '))
descuento = compra * 0.15
precio_final = compra - descuento

if compra > 1000:
    print(f'Ha recibido un descuento de 15%, paga en total: {precio_final}')
else:
    print(f'Usted ha pagado el precio regular: {compra}')

# Ejercicio 5

year = int(input(f'Ingrese el año: '))

 (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
'''
# Ejercicio 8
'''
#Ejercicio 9
print("\nBienvenido al programa de becas universitarias.")

promedio = float(input("Ingrese la primera nota del estudiante: "))
ingresos = float(input("Ingrese los ingresos mensuales del estudiante: "))
reportes_disciplinarios = bool(input("¿El estudiante tiene reportes disciplinarios? (true/false): ").lower())

if (promedio >= 8.5 and ingresos < 2000) and not reportes_disciplinarios:
    print("\nEl estudiante es elegible para la beca.")

else:
    print("\nEl estudiante no es elegible para la beca.")
'''