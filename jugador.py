class Jugador():
    def __init__(self,nombre):
        self.nombre = nombre
        self.puntos = 0
        self.mano = []
        self.estado = ""

    def mostrarMano(self):
        a = 0
        for m in self.mano:
            print(a,m)
            a+=1

    def Uno(self):
        if len(self.mano) == 2:
            print("Uno")
            self.estado = "Uno"

        else:
            print("Solo puedes decir uno cuando jugaras la penultima carta")

    def mostrarOpciones(self):
        print("Presiona 'r' para robar una carta")
        print("Presiona 'q' para jugar carta")
        print("Presiona 'w' para decir Uno y jugar la penultima carta")

    def jugarCarta(self,opcion):
        jugada = self.mano[opcion]
        self.mano.remove(self.mano[opcion])
        return jugada

    def verificarPuntos(self,jugadores):
        for e in jugadores:
            if e.puntos > 500:
                return True,e.nombre
        return False

    def sumarPuntos(self,jugadores,jugador):
        for e in jugadores.mano:
            jugador.puntos+=e[0]


try:
    while True:
        totalJugadores = int(input("¿Cuantos jugadores participaran?: "))
        if totalJugadores < 2 or totalJugadores > 10:
            totalJugadores = int(input("¿Cuantos jugadores participaran?: "))

        else:
            jugadores = []
            for a in range(totalJugadores):
                nombre = input("Nombre del jugador: ").capitalize()
                jugador = Jugador(nombre)
                jugadores.append(jugador)
                
            break

except:
    print("Introduciste una letra")
