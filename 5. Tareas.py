# Ejercicio 1

nota1 = float(input(f'Ingrese la primera calificacion -> '))
nota2 = float(input(f'Ingrese la segunda calificacion -> '))
nota3 = float(input(f'Ingrese la tercera calificacion -> '))
nota4 = float(input(f'Ingrese la cuarta calificacion -> '))

notas = (6.0, 10.0)

notas_total = [
    nota1,
    nota2, 
    nota3,
    nota4
]

for n in notas_total:

    if notas[0] <= n <= notas[1]:
        print('Ha aprobado')
    else:
        print('Ha reprobado')





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



# Ejercicio 3

presupuesto = float(input('Ingrese su presupuesto -> '))

canasta = []

tupla = [
    ('laptop', 150), 
    ('nevera', 500), 
    ('telefono', 99.99), 
    ('audifono', 49.99), 
    ('teclado', 15.50)
]

for t in tupla:
    if presupuesto>=t[1]:
        print(t[0])
        canasta.append(t[0])

compra =  input('Ingrese su producto -> ').lower()

if compra in canasta:
    print(f'Puedes comprar {compra}')
else:
    print(f'No puedes comprar {compra}')
  


# Ejercicio 4
print(f'\nBienvenido al cajero automatico')
saldo = 1000

operacion = (
    '1',
    '2',  
    '3',
    '4'
)
historial = []

usuario = input('Que operacion desea realizar \n1.Ingresar dinero en la cuenta. \n2.Retirar dinero de la cuenta. \n3.Mostrar dinero disponible. \n4.Salir. \n-> ')

while usuario != '4':

    if usuario not in operacion:
        print("Opcion invalida\n")

    elif usuario == '1':
        ingreso = int(input(f'Cuanto dinero desea ingresar -> '))
        saldo += ingreso
        print(f'Se ha depositado {ingreso}\n')
        historial.append(f'Ingreso -> {ingreso}')

    elif usuario == '2':
        retirar = int(input(f'Cuanto dinero desea retirar -> '))

        if retirar <= saldo:
            saldo -= retirar
            print(f'\nHa retirado {retirar}\n')
            historial.append(f'Retiro -> {retirar}')
        else:
            print('\nNo tienes dinero suficiente\n')

    elif usuario == '3':
        print(f'\nEste es su saldo -> {saldo}\n')
        historial.append(f'Consulta de saldo -> {saldo}')

    usuario = input('Que operacion desea realizar \n1.Ingresar dinero en la cuenta. \n2.Retirar dinero de la cuenta. \n3.Mostrar dinero disponible. \n4.Salir. \n-> ')

print(f'Estos son todos los movimientos que hizo -> {historial}')
print('Gracias por usar el cajero')

# Ejercicio 5

print('Evaluador de Contraseñas 🔐')

usuario = input('Ingresa contraseñas separadas por comas -> ')
lista = usuario.split(',')

longitud = (8, 20)

seguras = []

for contraseña in lista:

    contraseña = contraseña.strip()

    if len(contraseña) >= longitud[0] and len(contraseña) <= longitud[1]:
        
        if '@' in contraseña or '#' in contraseña or '$' in contraseña or '%' in contraseña:
            seguras.append(contraseña)

print('\nContraseñas seguras:')
print(seguras)

# Ejercicio 6


print('Bienvenido a Simulador de Duelo por Turnos ⚔️')

hp = [100, 100]

ataques = (5, 10, 20)

while hp[0] > 0 and hp[1] > 0:
    usuario = input(f'Que ataque desea hacer -> 1. ATAQUE BASICO {ataques[0]}, 2. ULTIMATE {ataques[2]}, 3.ATAQUE ELEMENTAL {ataques[1]} -> ').lower()
    
    if usuario == 'ataque basico':
        hp[1] -= ataques[0]
        print(f'Le hiciste {ataques[0]} de daño a la maquina')
    elif usuario == 'ultimate':
        hp[1] -= ataques[2]
        print(f'Le hiciste {ataques[2]} de daño a la maquina')
    elif usuario == 'ataque elemental':
        hp[1] -= ataques[1]
        print(f'Le hiciste {ataques[1]} de daño a la maquina')
    else:
        print('Ninguna opcion es valida perdiste el turno')

    print(f'Vida actual de la maquina: {hp[1]}')

    if hp[1] > 0:
        print('Turno de la maquina')
        hp[0] -= ataques[1]
        print(f'La maquina te hizo daño, tu vida es {hp[0]}')

# resultado final
if hp[0] > 0:
    print(f'El ganador eres tu con vida {hp[0]}')
else:
    print(f'El ganador es la maquina con vida {hp[1]}')