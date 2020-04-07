from card_pack import  *
from player import *
import os
import time
class Mesa():
    def accion(self,jugadores):
        print(" ")
        print(" ")
        self.__repJugadores(jugadores)
        print(" ")

    def __repJugadores(self,jugadores):
        for a in jugadores:
            print("{} : {}  {} ".format(a.nombre,a.puntos,a.estado))

    def repCartas(self,carta):
        print("En la mesa hay: \n{}".format(carta))
        return carta

    def validarCarta(self,jugada,carta):
        if carta[0] == jugada[0] or carta[1] == jugada[1]:
            return True
        
        elif jugada[0] == "+ 4" or jugada[0] == "Elegir color":
            return True
            

        else:
            return False



    def inicial(self,barajas):
        rango = randint(0,len(barajas.mazo)-1)
        check = barajas.mazo[rango]
        while check[0] in ["+ 2","Retorno","Intermision","+ 4","Elegir color"]:
            rango = randint(0,len(barajas.mazo)-1)
            check = barajas.mazo[rango]
            

        print("En la mesa hay: \n{}".format(barajas.mazo[rango]))
        return barajas.mazo[rango]
        barajas.mazo.remove(barajas.mazo[rango])







#jugadores[s] = especiales.intermision(jugadores)

tablero = Mesa()
tablero.accion(jugadores)
barajas.repartir(jugadores)
rondaIniciada = True
jugada = None
