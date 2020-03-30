
from random import randint

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



class Cartas():
    def __init__(self):
        self.lista = []
        self.color = ""
    def generar(self):
        self.__generarComodines()
        for a in range(10):
            if a!= 0:
                self.lista.append([a,self.color])
                self.lista.append([a,self.color])
    

            else:
                self.lista.append([a,self.color])

    def __generarComodines(self):
        comodines = ["Retorno","Intermision","+ 2"]
        for c in comodines:
            self.lista.append([c,self.color])
            self.lista.append([c,self.color])

class CartasComodines():
    def __init__(self):
        self.color = "Negro"
        self.lista = []

    def generar(self):
        for a in range(0,8):
            if a < 4:
                self.lista.append(["+ 4",self.color])
            else:
                self.lista.append(["Elegir color",self.color])

    def validar(self,tablero,jugador):
        cartaMesa = tablero.repCartas()
        for a in jugador.mano:
            if a[0] == cartaMesa[0] or a[1] == cartaMesa[1]:
                return False
        
        return True




class CartasRojas(Cartas):

    def __init__(self):
        self.lista = []
        self.color = "Rojo"



class CartasAzules(Cartas):
    def __init__(self):
        self.lista = []
        self.color = "Azul"


class CartasVerdes(Cartas):
    def __init__(self):
        self.lista = []
        self.color = "Verde"


class CartasAmarillas(Cartas):
    def __init__(self):
        self.lista = []
        self.color = "Amarillo"


especiales = CartasComodines()
rojas = CartasRojas()
azules = CartasAzules()
verdes = CartasVerdes()
amarillas = CartasAmarillas()
lista = [rojas,azules,verdes,amarillas,especiales]
listaCartas = []

def generarListas(lista):
    cartas = []
    for f in lista:
        f.generar()
        cartas.append(f.lista)

    return cartas


listaCartas = generarListas(lista)

barajas = Mazo()
barajas.llenar_mazo(listaCartas)
