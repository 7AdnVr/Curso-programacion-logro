import random

class Personaje:
    def __init__(self, nombre, salud, ataque):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque

    def recibir_dano(self, dano):
        self.salud -= dano


class Guerrero(Personaje):
    def ataque_pesado(self, objetivo):
        if random.randint(0, 1) == 1:
            objetivo.recibir_dano(self.ataque * 2)
        else:
            pass


class Curandero(Personaje):
    def accion_turno(self, objetivo):
        if self.salud < 20:
            self.salud += 10
        else:
            objetivo.recibir_dano(self.ataque)


messi = Guerrero("Guerrero", 100, 15)
ronaldo = Curandero("Curandero", 80, 10)

while messi.salud > 0 and ronaldo.salud > 0:
    messi.ataque_pesado(ronaldo)
    if ronaldo.salud > 0:
        ronaldo.accion_turno(messi)

if messi.salud > 0:
    print("Gana", messi.nombre)
else:
    print("Gana", ronaldo.nombre)