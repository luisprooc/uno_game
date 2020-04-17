print(" ██╗   ██╗███╗   ██╗ ██████╗ \n ██║   ██║████╗  ██║██╔═══██╗ \n ██║   ██║██╔██╗ ██║██║   ██║ \n ██║   ██║██║╚██╗██║██║   ██║ \n ╚██████╔╝██║ ╚████║╚██████╔╝ \n ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ \n ")

print(" It is a game that is played from 2 to 10 players \n as each player receives 7 cards to start. \n Your objective is to reach 500 points to defeat your teammates. \n  \n")


print(' ________ ________ ________ ________ ________ ________ ________ ________ ________ \n """""""" """""""" """""""" """""""" """""""" """""""" """""""" """""""" """"""""')

from table import *



while True:
    for s in range(0,len(players)):
        if players[s].notOmmited:
            specials.reSkip(players)
            os.system("cls")
            board.repPlayers(players)
            if roundStarted:
                card = board.initial(cardPack)
                roundStarted = False
            
            else:
                board.repCard(card)
                
            print("{} your hand is  :\n".format(players[s].name))
            players[s].showHand()
        
            players[s].showOptions()
            desicion = input("What do you want to do?: ")
            while desicion not in ["q","r","w"]:
                os.system("cls")
                board.repPlayers(players)
                if roundStarted:
                    card = board.initial(cardPack)
                    roundStarted = False
            
                else:
                    board.repCard(card)

                print("{} your hand is :".format(players[s].name))
                players[s].showHand()
                players[s].showOptions()
                desicion = input("What do you want to do?: ")

            if desicion == "q":
                try:
                    option = int(input(" what card do you want to play? :  "))
                    play = players[s].playCard(option)
                    if play[0] in cardPack.cardsValue:
                        if board.validateCard:
                            if play[0] == "Return":
                                p = specials.affected(players,players[s])
                                players.returnCard(players,p)

                            elif play[0] == "Choose color":
                                specials.showColors()
                                color = input("Choose a color: ")
                                specials.changeColor(play,specials.optionColor(color))

                            elif play[0] == "Intermission":
                                p = specials.affected(players,players[s])
                                specials.Skip(p)
                                print("{} has been skip".format(p.name))
                                time.sleep(3)

                            elif play[0] == "+ 2":
                                p = specials.affected(players,players[s])
                                specials.take2(p,cardPack)
                                print("{} have used + 2 on you ".format(players[s].name))
                                specials.Skip(p)
                                print("{} has been skip".format(p.name))
                                time.sleep(4)

                            
                            elif play[0] == "+ 4":
                                specials.showColors()
                                color = input("Choose a color: ")
                                specials.changeColor(play,specials.optionColor(color))
                                p = specials.affected(players,players[s])
                                validate = specials.noCard(card,players[s])
                                specials.take4(players[s],p,validate,cardPack)
                                time.sleep(4)
                                


                            

                        card = play
                        board.repCard(card)
                        
                    elif board.validateCard(play,card):
                        card = play
                        board.repCard(card)
                    
                    else:
                        players[s].hand.append(play)
                        print("You have been penalized for incorrect play")
                        cardPack.steal(players[s])
                        time.sleep(2)
                    
                except:
                    print("watch good the longitude your hand \n Penalized for not paying  attention to your hand")
                    time.sleep(2)

            elif desicion == "r":
                cardPack.steal(players[s])
                time.sleep(2)
                
            else:
                try:
                    players[s].Uno()
                    option = int(input(" what card do you want to play? :  "))
                    play = players[s].playCard(option)
                    if play[0] in cardPack.cardsValue:
                        if board.validateCard:
                            if play[0] == "Return":
                                players.reverse()

                            elif play[0] == "Choose color":
                                specials.showColors()
                                color = input("Choose a color: ")
                                specials.changeColor(play,specials.optionColor(color))


                        card = play
                        board.repCard(card)
                        
                    elif board.validateCard(play,card):
                        card = play
                        board.repCard(card)
                    
                    else:
                        players[s].hand.append(play)
                        print("You have been penalized for incorrect play")
                        cardPack.steal(players[s])
                        time.sleep(2)
                    
                except:
                    print("watch good the longitude your hand \n Penalized for not paying  attention to your hand ")
                    time.sleep(2)

                

            if len(players[s].hand) >= 2 and players[s].state == "Uno":
                players[s].state = ""

            if len(players[s].hand) == 1 and players[s].state == "":
                print("You have been penalized for not saying 'Uno' ")
                cardPack.steal(players[s])
                time.sleep(2)
            

            if len(players[s].hand) == 0:
                print("{} has won this round".format(players[s].name))
                players[s].addPoints(players,players[s],cardPack)
                #tablero = Mesa()
                #tablero.accion(jugadores)
                players[s].restartHand(players)
                players[s].restartStates(players)
                cardPack.handOut(players)
                roundStarted = True
                print("New round")
                time.sleep(2)
                os.system("cls")



            if players[s].checkPoints(players):
                print("{} has won this match".format(players[s].name))
                break


    

            
