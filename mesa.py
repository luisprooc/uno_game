from baraja import *
from random import randint
class Mesa(object):
    def accion(self,jugadores,mazo):
        self.__repJugadores(jugadores)
        print(" ")



    def __repJugadores(self,jugadores):
        for a,b in jugadores:
            print("{} : {}".format(a,b))

    def repCartas(self,carta):
        print("En la mesa hay: \n{}".format(carta))

    def inicial(self,barajas):
        rango = randint(0,len(barajas.mazo)-1)
        self.repCartas(barajas.mazo[rango])
        barajas.mazo.remove[rango]








print(len(barajas.mazo))

Juan = "Juan"
Pedro = "Pedro"

tablero = Mesa()
tablero.accion([[Juan,20],[Pedro,30]],[barajas.mazo])



