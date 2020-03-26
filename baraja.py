
class Mazo(object):
    def __init__(self):
        self.mazo = []
    def llenar_mazo(self,cartas):
        for e in cartas:
            self.mazo += e


class Cartas(object):
    def __init__(self):
        self.lista = []
        self.color = ""
    def generar(self):
        for a in range(10):
            if a!= 0:
                self.lista.append([a,self.color])
                self.lista.append([a,self.color])
    

            else:
                self.lista.append([a,self.color])




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

print(azules.lista,rojas.lista,verdes.lista)
