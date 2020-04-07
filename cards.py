class Cards():
    def __init__(self):
        self.list = []
        self.color = ["Red","Blue","Green","Yellow"] 
        self.colors = 0

    def generateRed(self):
        self.__generateComodines()
        for a in range(10):
            if a!= 0:
                self.list.append([a,self.color[self.colors]])
                self.list.append([a,self.color[self.colors]])
    

            else:
                self.list.append([a,self.color[self.colors]])

        self.colors+= 1

    def __generateComodines(self):
        wildcards= ["Retorno","Intermision","+ 2"]
        for c in wildcards:
            self.list.append([c,self.color[self.colors]])
            self.list.append([c,self.color[self.colors]])

    
    def generateBlue(self):
        self.__generateComodines()
        for a in range(10):
            if a!= 0:
                self.list.append([a,self.color[self.colors]])
                self.list.append([a,self.color[self.colors]])

            else:
                self.list.append([a,self.color[self.colors]])

        self.colors+= 1


    def generateGreen(self):
        self.__generateComodines()
        for a in range(10):
            if a!= 0:
                self.list.append([a,self.color[self.colors]])
                self.list.append([a,self.color[self.colors]])

            else:
                self.list.append([a,self.color[self.colors]])

        self.colors+= 1


    def generateYellow(self):
        self.__generateComodines()
        for a in range(10):
            if a!= 0:
                self.list.append([a,self.color[self.colors]])
                self.list.append([a,self.color[self.colors]])

            else:
                self.list.append([a,self.color[self.colors]])

        self.colors+= 1


            
    
    


commonCards = Cards()
commonCards.generateBlue()
commonCards.generateGreen()
commonCards.generateRed()
commonCards.generateYellow()
