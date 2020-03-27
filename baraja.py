

from random import randint

class Mazo(object):
    def __init__(self):
        self.mazo = []
    def llenar_mazo(self,cartas):
        for e in cartas:
            self.mazo += e

    def robar(self):
        rango = randint(0,len(self.mazo)-1)
        print("tomaste la carta{}".format(self.mazo[rango]))
        self.mazo.remove(self.mazo[rango])

    def repartir(self):
        for s in range(0,7):
            rango = randint(0,len(self.mazo)-1)
            print("{}".format(self.mazo[rango]))
            self.mazo.remove(self.mazo[rango])



class Cartas(object):
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
        comodines = ["Retroceso","Omitir","+ 2"]
        for c in comodines:
            self.lista.append([c,self.color])
            self.lista.append([c,self.color])




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


rojas = CartasRojas()
rojas.generar()

azules = CartasAzules()
azules.generar()

verdes = CartasVerdes()
verdes.generar()

amarillas = CartasAmarillas()
amarillas.generar()

barajas = Mazo()
barajas.llenar_mazo([rojas.lista,verdes.lista,azules.lista,amarillas.lista])
barajas.repartir()
print(" ")
print(barajas.mazo)