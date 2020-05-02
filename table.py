from card_pack import  *
from player import *
class Table():
    
    def repPlayers(self,players):
        for a in players:
            print("{} : {}  {} ".format(a.name,a.points,a.state))
        print("\n")

    def repCard(self,card):
        print("In the table there is: \n{} \n".format(card))
        return card

    def validateCard(self,play,card):
        if card[0] == play[0] or card[1] == play[1]:
            return True
        
        elif play[0] == "+ 4" or play[0] == "Choose color":
            return True
            

        else:
            return False



    def initial(self,cardPack):
        choose = randint(0,len(cardPack.deck)-1)
        check = cardPack.deck[choose]
        while check[0] in ["+ 2","Return","Intermission","+ 4","Choose color"]:
            choose = randint(0,len(cardPack.deck)-1)
            check = cardPack.deck[choose]
            

        print("In the table there is: \n{} \n".format(cardPack.deck[choose]) )
        return cardPack.deck[choose]
        cardPack.deck.remove(cardPack.deck[choose])


    def rules(self):
        allRules = " ..................................................  \n - Incorrect play: steal a card. \n - Don't say 'Uno' before to play the penultimate card: steal a card. \n - Enter a number that exceeds the length of your hand: You don't play this turn. \n - you must only play +4 when you have no cards matching the card on the table: otherwise you will take six cards. \n  .................................................. "
        
        print("Rules\n",allRules)
    







board = Table()
cardPack.handOut(players)
board.repPlayers(players)
roundStarted = True
play = None






board.rules()

ready = input("Press any key to start: ")
