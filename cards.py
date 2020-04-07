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


