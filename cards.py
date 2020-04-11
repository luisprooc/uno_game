class Cards():
    def __init__(self):
        self.list = []
        self.colors = ["Red","Blue","Green","Yellow"] 

    def generate(self):
        self.__generateComodines()
        for c in self.colors:
            for a in range(10):
                if a!= 0:
                    self.list.append([a,c])
                    self.list.append([a,c])
        

                else:
                    self.list.append([a,c])



    def __generateComodines(self):
        wildcards= ["Return","Intermission","+ 2"]
        for color in self.colors:
            for c in wildcards:
                self.list.append([c,color])
                self.list.append([c,color])

 
    


commonCards = Cards()
commonCards.generate()
