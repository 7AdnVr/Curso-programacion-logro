
'''
import math

radio = int(input('Ingrese su radio -> '))
pi = 3.1416

area = math.pi * radio**2
longitud = 2 * math.pi * radio



print(f"el area es {area:.2f} y su longittud es {longitud:.2f}")
'''
print(f'\nBienvenido al cajero automatico')
saldo = 1000

operacion = input('Que operacion desea realizar \n1.Ingresar dinero en la cuenta. \n2.Retirar dinero de la cuenta. \n3.Mostrar dinero disponible. \n4.Salir. \n-> ')

if operacion == '1':
    ingreso = int(input(f'Cuanto dinero desea ingresar -> '))
    saldo += ingreso
    print(f'Se ha depositado {ingreso}')
elif operacion == '2':
    retirar = int(input(f'Cuanto dinero desea retirar ->'))
    if retirar <= saldo:
        saldo -= retirar
        print(f'Ha retirado {retirar}')
    else:
        print('No tienes money')
elif operacion == '3':
    print(f'Este su salgo -> {saldo}')
elif operacion == '4':
    print('Vuelva pronto')
        
    
