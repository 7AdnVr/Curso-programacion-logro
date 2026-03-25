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