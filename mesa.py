from baraja import  *
class Mesa():
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
        barajas.mazo.remove(barajas.mazo[rango])







Juan = "Juan"
Pedro = "Pedro"

tablero = Mesa()
tablero.accion([[Juan,0],[Pedro,0]],[barajas.mazo])
tablero.inicial(barajas)



