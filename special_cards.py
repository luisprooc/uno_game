
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

    def noCard(self,card,player):
        for a in player.hand:
            if a[0] ==  card[0] or a[1] ==  card[1]:
                return False
        
        return True

    def Skip(self,player):
        player.notOmmited= False



    def returnCard(self,players,affected):
        players.reverse()
        players.remove(affected)
        players.insert(0,affected)
        print(players)


    def changeColor(self,play,color):
        change = play
        change[1] = color
        return play
        

    def showColors(self):
        print(" Press 1 to choose red color \n Press 2 to choose blue color \n Press 3 to choose green color \n Press 4 to choose yellow color \n Press any key for random color")


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


    def take2(self,player,cardPack):
        print("{} you have taken 2 cards \n".format(player.name))
        for a in range(2):
            cardPack.steal(player)
                            

    
    def affected(self,players,player):
        for x in range(-1,len(players)-1):
            if players[x] == player:
                p = players[x+1]
                return p

    def reSkip(self,players):
        for p in players:
            p.notOmmited = True

    
    def take4(self,player,nextPlayer,validate,cardPack):
        if validate:
            print("{} you have taken 4 cards \n".format(nextPlayer.name))
            for t in range(5):
                cardPack.steal(nextPlayer)

            self.Skip(player)
        else:

            print("{} you have taken 6 cards \n".format(player.name))
            for t in range(7):
                cardPack.steal(player)

        return ""






        





specials = WildCards()
specials.generate()


##test ####
"""
names = ["Juan","Marco","Lucas","Maria"]
affected = specials.affected(names,"Juan")
specials.returnCard(names,affected)
"""


