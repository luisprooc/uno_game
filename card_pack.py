
from cards import *
from special_cards import *
class Deck():
    def __init__(self):
        self.deck = []
        self.cardsValue = {"+ 2":20,"Return":20,"Intermission":20,"+ 4":50,"Choose color":50}

    def fillDeck(self,cards):
        for e in cards:
            self.deck += e

    def steal(self,player):
        choose = randint(0,len(self.mazo)-1)
        print("You took the card{}".format(self.deck[choose]))
        player.hand.append(self.deck[choose])
        self.deck.remove(self.deck[choose])

    def handOut(self,players):
        for j in players:
            for s in range(0,7):
                choose = randint(0,len(self.deck)-1)
                j.hand.append(self.deck[choose])
                self.deck.remove(self.deck[choose])





cardPack = Deck()
cardList = [specials.list,commonCards.list]
cardPack.fillDeck(cardList)


