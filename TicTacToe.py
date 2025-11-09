# TicTacToe.py
# Versión básica - Rama main

def MostrarTablero(tablero):
    print()
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print("--+---+--")
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print("--+---+--")
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])
    print()

def VerificarGanador(tablero, jugador):
    combinaciones = [
        (0,1,2), (3,4,5), (6,7,8),  # Filas
        (0,3,6), (1,4,7), (2,5,8),  # Columnas
        (0,4,8), (2,4,6)            # Diagonales
    ]
    for a,b,c in combinaciones:
        if tablero[a] == tablero[b] == tablero[c] == jugador:
            return True
    return False

def Juego():
    tablero = [" "] * 9
    jugador_actual = "X"

    for turno in range(9):
        MostrarTablero(tablero)
        print(f"Turno del jugador {jugador_actual}")
        movimiento = int(input("Elige una posición (1-9): ")) - 1

        if tablero[movimiento] != " ":
            print("Posición ocupada. Intenta de nuevo.")
            continue

        tablero[movimiento] = jugador_actual

        if VerificarGanador(tablero, jugador_actual):
            MostrarTablero(tablero)
            print(f"¡Jugador {jugador_actual} gana!")
            return

        jugador_actual = "O" if jugador_actual == "X" else "X"

    MostrarTablero(tablero)
    print("¡Empate!")

if __name__ == "__main__":
    Juego()
