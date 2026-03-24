# Ejercicio 1
nombre_usuario = "Adrian"
edad = 19
hobby = "jugar counter strike 2"
color_favorito = "azul"

print(f"Mi nombre es {nombre_usuario}, tengo {edad} años y me gusta {hobby}. Mi color favorito es {color_favorito}.")

# Ejercicio 2
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))
area = base * altura
perimetro = 2 * (base + altura)

print("El area del rectangulo es:", area)
print("el perimetro del rectangulo es:", perimetro)

# Ejercicio 3
num1 = 5
num2 = 10
suma = num1 + num2
resta =num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 
division_entera = num1 // num2
modulo = num1 % num2
print(f"la resta de {num1} y {num2} es: {resta}")
print(f"la multiplicacion de {num1} y {num2} es: {multiplicacion}")
print(f"la division de {num1} y {num2} es: {division}")
print(f"la division entera de {num1} y {num2} es: {division_entera}")
print(f"el modulo de {num1} y {num2} es: {modulo}") 

# Ejercicio 4
tasa_bs = "460"
cantidad_usd = int(input("Ingrese la cantidad de USD a convertir:"))
cantidad = cantidad_usd * int(tasa_bs)
print(f"{cantidad_usd} USD a {cantidad} Bs")

# Ejercicio 5
especie = "Loro"
nombre = "Pepe"
edad = 2
print(f"Mi mascota es un {especie}, se llama {nombre} y tiene {edad} años.")

# Ejercicio 6
exam1 = 6
exam2 = 7
exam3 = 9
resultado = exam1 + exam2 + exam3
print(f"El resultado promedio de los examenes es: {resultado/3} ")

# Ejercicio 7
edad = 19
edad_10 = edad + 10
edad_result = edad + 2050 - 2026
print(f"Actualmente tengo {edad} años, tendre en 10 años: {edad_10}")
print(f"Tengo {edad} años en el 2026, tendre en el año 2050: {edad_result}")
print(f"En 2050 tengo: {edad_result} años")

# Ejercicio 8
es_estudiante = True
tiene_trabajo = False

print(f"Soy estudiante: {es_estudiante} y tengo trabajo: {tiene_trabajo}")

# Ejercicio 9
la = "Hola"
pe = "Mundo"
print(f"{la} {pe}")