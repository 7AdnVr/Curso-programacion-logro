# 
print("="*40)
print('Simulador de Cesta de Compra en Python! 🛒💻')
print("="*40)

opciones = (
    'renunciar',
    'agregar',
    'mostrar',
    'eliminar',
    'calcular'
)
nombre = []
precio = []

nombre_precio = nombre+precio


usuario = input(f'Que operacion desea realizar \n🔹 AGREGAR un nuevo elemento ➕ \n🔹 MOSTRAR el contenido de la cesta de la compra 🧺 \n🔹 ELIMINAR un elemento ❌ \n🔹 CALCULAR el total de la compra 💰 \n🔹 RENUNCIAR 👋 para salir del programa \n -> ').lower()

while usuario != 'renunciar':

    if usuario not in opciones:
        print('\nNinguna opcion es valida\n')

    elif usuario == 'agregar':
        usuario = input(f'Que desea agregar -> ')
        nombre.append(usuario)
        print(f'Se ha agregado correctamente')
        usuario = float(input(f'Que precio desea ponerle -> '))
        precio.append(usuario)
        print(f'Se ha agregado correctamente')

    elif usuario == 'calcular':
        print(f'{nombre}{precio}')

    elif usuario == 'eliminar':
        usuario = input(f'Que desea eliminar de -> ')
        