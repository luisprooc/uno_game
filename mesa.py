class Mesa(object):
    def accion(self,jugadores,mazo):
        self.__repJugadores(jugadores)
        print(" ")
        self.__repCartas(mazo)



    def __repJugadores(self,jugadores):
        for a,b in jugadores:
            print("{} : {}".format(a,b))

    def __repCartas(self,mazo):
        for x in mazo:
            print("En la mesa hay: \n{}".format(x))







Juan = "Juan"
Pedro = "Pedro"

mesa = Mesa()
mesa.accion([[Juan,20],[Pedro,30]],["3 Rojo"])



