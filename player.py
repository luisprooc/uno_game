class Player():
    def __init__(self,name):
        self.name = name
        self.points = 0
        self.hand = []
        self.state = ""
        self.notOmmited = True
        self.retired = ""

    def showHand(self):
        a = 0
        for m in self.hand:
            print(a,m)
            a+=1
        
        print("\n")

    def Uno(self):
        if len(self.hand) == 2:
            print("Uno")
            self.state = "Uno"

        else:
            print("You can only say one as you play the penultimate card")

    def showOptions(self):
        print("Press 'q' to play card \nPress 'w' to say Uno and play the penultimate card \nPress 'e' to retire\nPress 'r' to draw a card\n")

    def playCard(self,option):
        play = self.hand[option]
        self.hand.remove(self.hand[option])
        return play

    def checkPoints(self,players):
        for e in players:
            if e.points > 500:
                return True
        return False

    def addPoints(self,players,player,cardPack):
        for j in players:
            for e in j.hand:
                if e[0] not in cardPack.cardsValue:
                    player.points+=e[0]

                else:
                    player.points+= cardPack.cardsValue[e[0]]

    
    def restartHand(self,players):
        for player in players:
            player.hand.clear()
        
            


    def restartStates(self,players):
        for e in players:
            e.state = ""

    def giveUp(self,player):
        player.retired = "Retired"

    def checkRetired(self,players):
        cont = 0
        for r in players:
            if r.retired == "":
                cont+= 1

        if cont == 1:
            return True
        
        else:
            return False
        


while True:
    try:
        totalPlayers = int(input("How many players will participate?: "))
        while  totalPlayers < 2 or  totalPlayers > 10:
            print("The number of players must be between 2 to 10.")
            totalPlayers  = int(input("How many players will participate?: "))


        players = []
        for a in range(totalPlayers):
            name = input("Player's name : ").capitalize()
            player = Player(name)
            players.append(player)

        break 

    except:
        print("You enter a letter")
    





