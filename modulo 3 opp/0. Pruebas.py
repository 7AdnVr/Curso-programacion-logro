class estudiante:
    # Atributos de clase
    universidad = "Ninguna"
    # Atributos  de instancia es al constructor
    def __init__(self, nombre, carrera, cedula, edad):
        self.nombre = nombre
        self.carrera = carrera
        self.cedula = cedula
        self.edad = edad

    # Metodo de instancia

    def estudiar(self, estudio):

        estudio = input('Estas estudiando? si/no -> ')
        if estudio.lower() == 'si':
            print('sigue estudiando!')
        else:
            print('Comienza a estudiar!')

class trabajo:
    # Atributo de clase

    empresa = 'Ninguna'

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo 
        self.salario = salario

    def cobrar(self):
        empresa = input('En que pasa trabajas? -> ')
        if empresa.lower == 'ninguna':
            print('No estas trabajando')
        elif empresa.lower == 'google':
            cobro = input('ya cobraste -> si/no -> ')
            if cobro == 'si':
                print('Felicidades')
            else:
                print('Ya cobraras')
        print(f'{self.nombre} ha cobrado de su salario {self.salario}$')
        
     
persona1 = estudiante("Adrian", "Informatica", 31989067, 20)
trabajador1 = trabajo('Adrian', 'Vagar', 1000)



trabajador1.cobrar()