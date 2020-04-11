
from random import randint
class WildCards():
    def __init__(self):
        self.color = "Black"
        self.list = []

    def generate(self):
        for a in range(0,8):
            if a < 4:
                self.list.append(["+ 4",self.color])
            else:
                self.list.append(["Choose color",self.color])

    def take4(self,board,player):
        tableCard = board.repCards()
        for a in player.hand:
            if a[0] ==  tableCard[0] or a[1] ==  tableCard[1]:
                return False
        
        return True

    def intermission(self,players):
        b = 0
        return players[b+1]

    def returnCard(self,players):
        return players.reverse()

    def changeColor(self,play,color):
        play[1] = color
        return play
        play[1] = "Black"

    def showColors(self):
        print("Press 1 to choose red color \n Press 2 to choose blue color \n Press 3 to choose green color \n Press 4 to choose yellow color \n Press any key for random color")


    def optionColor(self,color):
        chosenColor = ""
        if color == "1":
            chosenColor = "Red"

        elif color == "2":
            chosenColor= "Blue"

        elif color == "3":
            chosenColor= "Green"
        
        elif color == "4":
            chosenColor = "Yellow"

        else:
            colors = ["Red","Blue","Green","Yellow"]
            random = randint(1,4)
            chosenColor = colors[random]

        
        return chosenColor



specials = WildCards()
specials.generate()


