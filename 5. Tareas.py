prohibidos = ('admin', 'root', 'usuario', 'contrase', 'sex')

intentos = []

nombres = input(f'Crea tu nombre de usuario: ').lower()

while nombres in prohibidos:
    print("Ese nombre esta bloqueado ")
    intentos.append(nombres)

    nombres = input(f'Elige otro nombre: ').lower()

print('Valido')
print(f'intentos fallidos, {intentos}')



   


