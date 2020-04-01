print("██╗   ██╗███╗   ██╗ ██████╗")
print("██║   ██║████╗  ██║██╔═══██╗")
print("██║   ██║██╔██╗ ██║██║   ██║")
print("██║   ██║██║╚██╗██║██║   ██║")
print("╚██████╔╝██║ ╚████║╚██████╔╝")
print( "╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ")

print("  ")
print(" Es un juego que se juega de 2 a 10 jugadores")
print("  ")
print(" Donde cada jugador recibe 7 cartas al empezar")
print(" ")
print(" Tu objetivo es llegar a los 500 puntos para derrotar a tus compañeros")
print("  ")
print(" ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄")
print("▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌")
print("▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ")
print("▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ")
print("▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ")
print("▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ")
print(" ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀      ▐░▌     ")
print("          ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌     ")
print(" ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌▐░▌      ▐░▌      ▐░▌     ")
print("▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ")
print(" ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀         ▀  ▀         ▀       ▀      ")
print( "                                                                ")

print(                                                                                 )                                                                        
print("________ ________ ________ ________ ________ ________ ________ ________ ________")
print('"""""""" """""""" """""""" """""""" """""""" """""""" """""""" """""""" """"""""')
print(                                                                                  ) 
from mesa import *



while True:
    for s in range(0,len(jugadores)):
        os.system("cls")
        tablero.accion(jugadores)
        if rondaIniciada:
            carta = tablero.inicial(barajas)
            rondaIniciada = False
        
        else:
            tablero.repCartas(carta)
            
        print(" ")
        print("{} tu mano es :".format(jugadores[s].nombre))
        print("  ")
        jugadores[s].mostrarMano()
        print(" ")
        jugadores[s].mostrarOpciones()
        desicion = input("¿Que deseas hacer?: ")
        while desicion not in ["q","r","w"]:
            os.system("cls")
            tablero.accion(jugadores)
            if rondaIniciada:
                carta = tablero.inicial(barajas)
                rondaIniciada = False
        
            else:
                tablero.repCartas(carta)
            
            print(" ")
            print("{} tu mano es :".format(jugadores[s].nombre))
            print("  ")
            jugadores[s].mostrarMano()
            print(" ")

            jugadores[s].mostrarOpciones()
            desicion = input("¿Que deseas hacer?: ")

        if desicion == "q":
            opcion = int(input(" Que carta deseas jugar? :  "))
            jugada = jugadores[s].jugarCarta(opcion)
            if jugada[0] in barajas.valorCartas:
                if tablero.validarCarta:
                    if jugada[0] == "Retorno":
                        jugadores.reverse()

                    elif jugada[0] == "Elegir color":
                        especiales.mostrarColores()
                        color = input("Elige un color: ")
                        especiales.cambiarColor(jugada,especiales.opcionColor(color))


                carta = jugada
                tablero.repCartas(carta)
                
            elif tablero.validarCarta(jugada,carta):
                carta = jugada
                tablero.repCartas(carta)
            
            else:
                jugadores[s].mano.append(jugada)
                print("Haz sido penalizado por jugada incorrecta")
                barajas.robar(jugadores[s])
                time.sleep(2)

        elif desicion == "r":
            barajas.robar(jugadores[s])
            time.sleep(2)
            
        else:
            jugadores[s].Uno()
            opcion = int(input(" Que carta deseas jugar? :  "))
            jugada = jugadores[s].jugarCarta(opcion)
            if jugada[0] in barajas.valorCartas:
                if tablero.validarCarta:
                    if jugada[0] == "Retorno":
                        jugadores.reverse()


            if tablero.validarCarta(jugada,carta):
                carta = jugada
                tablero.repCartas(carta)
            
            else:
                jugadores[s].mano.append(jugada)
                print("Haz sido penalizado por jugada incorrecta")
                barajas.robar(jugadores[s])
                time.sleep(2)
            time.sleep(2)


        
        if len(jugadores[s].mano) == 0:
            print("{} ha ganado esta ronda".format(jugadores[s].nombre))
            #jugadores[s].sumarPuntos(jugadores,jugadores[s])
            tablero = Mesa()
            tablero.accion(jugadores)
            barajas.repartir(jugadores)
            rondaIniciada = True
            os.system("cls")


        if jugadores[s].verificarPuntos(jugadores):
            break
