class Player():
    def __init__(self,name):
        self.name = name
        self.points = 0
        self.hand = []
        self.state = ""

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
        print("Press 'r' to draw a card")
        print("Press 'q' to play card")
        print("Press 'w' to say Uno and play the penultimate card \n")

    def playCard(self,option):
        play = self.hand[option]
        self.hand.remove(self.hand[option])
        return play

    def checkPoints(self,players):
        for e in players:
            if e.points > 500:
                return True,
        return False

    def addPoints(self,players,player,cardPack):
        for j in players:
            for e in j.hand:
                if e[0] not in cardPack.cardsValue:
                    player.points+=e[0]

                else:
                    player.points+= cardPack.cardsValue[e[0]]

    
    def restartHand(self,players):
        for j in players:
            for e in j.hand:
                e = ""


    def restartStates(self,players):
        for e in players.state:
            e = ""
        


try:
    while True:
        totalPlayers = int(input("How many players will participate?: "))
        if totalPlayers  < 2 or  totalPlayers > 10:
            totalPlayers  = int(input("How many players will participate?: "))

        else:
            players = []
            for a in range(totalPlayers):
                name = input("Player's name : ").capitalize()
                player = Player(name)
                players.append(player)
                
            break

except:
    print("You entered a letter")




