presupuesto = float(input('Ingrese su presupuesto -> '))

canasta = []

tupla = [
    ('Laptop', 150), 
    ('Nevera', 500), 
    ('Telefono', 99.99), 
    ('Audifono', 49.99), 
    ('Teclado', 15.50)
]

for t in tupla:
    if presupuesto >= t[1]:
        print(t[0])
        canasta.append(t[0])

compra = input('Ingrese su producto -> ')

if compra in canasta:
    print("Puedes comprarlo")
else:
    print("No puedes comprarlo")