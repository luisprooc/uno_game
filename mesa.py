from baraja import  *
from jugador import *
class Mesa():
    def accion(self,jugadores,mazo):
        print(" ")
        print(" ")
        self.__repJugadores(jugadores)
        print(" ")

    def __repJugadores(self,jugadores):
        for a in jugadores:
            print("{} : {}".format(a.nombre,a.puntos))

    def repCartas(self,barajas):
        carta = barajas.mazo[0]
        print("En la mesa hay: \n{}".format(carta))


    def inicial(self,barajas):
        rango = randint(0,len(barajas.mazo)-1)
        print("En la mesa hay: \n{}".format(barajas.mazo[rango]))
        barajas.mazo.remove(barajas.mazo[rango])









tablero = Mesa()
tablero.accion(jugadores,[barajas.mazo])
barajas.repartir(jugadores)
tablero.inicial(barajas)
while True:
    for s in jugadores:
        print(" ")
        print("{} tu mano es :".format(s.nombre))
        print( "  ")
        s.mostrarMano()
        print(" ")
        input("¿Que carta deseas jugar?: ")
        print(" ")
        tablero.repCartas(barajas)