# Ejercicio 1 
precio_base = 57
precio_final = precio_base + (precio_base * 0.21) 
print(f"el precio con IVA es: {precio_final}")

# Ejercicio 2 
edad = int(input("Ingrese su edad: ")) 
multi = edad * 365 
print(f"Has vivido aproximadamente {multi} días.") 

# Ejercicio 3
pi = 3.1416
radio = float(input("Ingrese el radio del circulo: ")) 
perimetro = 2 * pi * radio 
print(f"La circunferencia del circulo es: {perimetro}") 

# Ejercicio 4
edad_mayor = int(input("Ingrese su edad: ")) 
print(f"¿Eres mayor de edad? {edad_mayor >= 18}") 

# Ejercicio 5
km = float(input("Ingrese la distancia en kilometros: "))
litros = float(input("Ingrese la cantidad de litros consumidos: "))
consumo = km / litros 
print(f"El rendimiento del motor es: {consumo} km/litros") 

# Ejercicio 6
numero = int(input("Ingrese un numero: "))
and_condition = (numero >= 10) and (numero <= 20)
print(f"¿{numero} esta entre 10 y 20? {and_condition}") 

# Ejercicio 7
dias = int(input("Ingrese los dias: ")) 
convertir = dias * 24 * 60 * 60 
print(f"{dias} dias son equivalentes a {convertir} segundos.") 

# Ejercicio 8
#Resuelve ax + b = 0
a = float(input("Ingrese el valor de a: ")) 
b = float(input("Ingrese el valor de b: ")) 
print(f"x = {-b/a}") 

# Ejercicio 9
peso = float(input("Ingrese su peso en kg: ")) 
altura = float(input("Ingrese su altura en metros: ")) 
imc = peso / (altura ** 2) 
print(f"Tu indice de masa corporal (IMC) es: {imc:.2f}") 

# Ejercicio 10
lag1 = input("Ingrese el primer texto:") 
lag2 = input("Ingrese el segundo texto:")
condition = len(lag1) > len(lag2) 
print(f"¿El primer texto es mas largo que el segundo? {condition}") 