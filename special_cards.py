
from random import randint
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

    def toma4(self,tablero,jugador):
        cartaMesa = tablero.repCartas()
        for a in jugador.mano:
            if a[0] == cartaMesa[0] or a[1] == cartaMesa[1]:
                return False
        
        return True

    def intermision(self,jugadores):
        b = 0
        return jugadores[b+1]

    def retorno(self,jugadores):
        return jugadores.reverse()

    def cambiarColor(self,jugada,color):
        jugada[1] = color
        return jugada

    def mostrarColores(self):
        print(" ")
        print("Presiona 1 para elegir color rojo")
        print("Presiona 2 para elegir color azul")
        print("Presiona 3 para elegir color verde")
        print("Presiona 4 para elegir color amarillo")
        print("Presiona cualquiera tecla para color aleatorio")
        print(" ")

    def opcionColor(self,color):
        colorElegido = ""
        if color == "1":
            colorElegido = "Rojo"

        elif color == "2":
            colorElegido = "Azul"

        elif color == "3":
            colorElegido = "Verde"
        
        elif color == "4":
            colorElegido = "Amarillo"

        else:
            aleatorio = randint(1,4)
            if aleatorio == 1:
                colorElegido = "Rojo"

            elif aleatorio == 2:
                colorElegido = "Azul"

            elif aleatorio == 3:
                colorElegido = "Verde"

            else:
                colorElegido = "Amarillo"

            return colorElegido

        
        return colorElegido




"""



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
"""
