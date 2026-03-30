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

usuario = input(f'Que operacion desea realizar \n🔹 AGREGAR un nuevo elemento ➕ \n🔹 MOSTRAR el contenido de la cesta de la compra 🧺 \n🔹 ELIMINAR un elemento ❌ \n🔹 CALCULAR el total de la compra 💰 \n🔹 RENUNCIAR 👋 para salir del programa \n -> ').lower()

while usuario != 'renunciar':

    if usuario not in opciones:
        print('\nNinguna opcion es valida\n')

    elif usuario == 'agregar':
        producto = input('Que desea agregar -> ')
        nombre.append(producto)

        valor = float(input('Que precio desea ponerle -> '))
        precio.append(valor)

        print('Se ha agregado correctamente\n')

    elif usuario == 'mostrar':
        if not nombre:
            print('\nNo tienes nada, agrega algo\n')
        else:
            print('\nLista de compra:')
            for i in range(len(nombre)):
                print(f'{i+1}. {nombre[i]} - ${precio[i]}')
            print()

    elif usuario == 'eliminar':
        if not nombre:
            print('\nNo hay nada para eliminar\n')
        else:
            print('\nLista de compra:')
            for i in range(len(nombre)):
                print(f'{i+1}. {nombre[i]} - ${precio[i]}')

            opcion = int(input('Numero del producto que quieres eliminar -> '))

            if 1 <= opcion <= len(nombre):
                indice = opcion - 1
                nombre.pop(indice)
                precio.pop(indice)
                print('Se ha eliminado correctamente\n')
            else:
                print('Numero invalido\n')

    elif usuario == 'calcular':
        total = 0
        for p in precio:
            total += p
        print(f'\nTotal a pagar: ${total}\n')

    usuario = input(f'Que operacion desea realizar \n🔹 AGREGAR un nuevo elemento ➕ \n🔹 MOSTRAR el contenido de la cesta de la compra 🧺 \n🔹 ELIMINAR un elemento ❌ \n🔹 CALCULAR el total de la compra 💰 \n🔹 RENUNCIAR 👋 para salir del programa \n -> ').lower()