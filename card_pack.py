from random import randint
from cards import *
from special_cards import *
class Mazo():
    def __init__(self):
        self.mazo = []
        self.valorCartas = {"+ 2":20,"Retorno":20,"Intermision":20,"+ 4":50,"Elegir color":50}
    def llenar_mazo(self,cartas):
        for e in cartas:
            self.mazo += e

    def robar(self,jugador):
        rango = randint(0,len(self.mazo)-1)
        print("tomaste la carta{}".format(self.mazo[rango]))
        jugador.mano.append(self.mazo[rango])
        self.mazo.remove(self.mazo[rango])

    def repartir(self,jugadores):
        for j in jugadores:
            for s in range(0,7):
                rango = randint(0,len(self.mazo)-1)
                j.mano.append(self.mazo[rango])
                self.mazo.remove(self.mazo[rango])

