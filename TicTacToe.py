# TicTacToe.py
# Versión mejorada con interfaz gráfica - Rama Feature

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.jugador_actual = "X"
        self.tablero = [" " for _ in range(9)]

        self.botones = []
        self.CrearInterfaz()

    def CrearInterfaz(self):
        tk.Label(self.root, text="Tic Tac Toe", font=("Arial", 18, "bold")).pack(pady=10)
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            boton = tk.Button(frame, text=" ", font=("Arial", 20), width=5, height=2,
                              command=lambda i=i: self.Jugada(i))
            boton.grid(row=i//3, column=i%3)
            self.botones.append(boton)

        self.label_turno = tk.Label(self.root, text=f"Turno del jugador {self.jugador_actual}", font=("Arial", 12))
        self.label_turno.pack(pady=10)

    def Jugada(self, i):
        if self.tablero[i] == " ":
            self.tablero[i] = self.jugador_actual
            self.botones[i].config(text=self.jugador_actual)

            if self.VerificarGanador():
                messagebox.showinfo("Fin del juego", f"¡Jugador {self.jugador_actual} gana!")
                self.Reiniciar()
                return

            if " " not in self.tablero:
                messagebox.showinfo("Empate", "¡Nadie gana!")
                self.Reiniciar()
                return

            self.jugador_actual = "O" if self.jugador_actual == "X" else "X"
            self.label_turno.config(text=f"Turno del jugador {self.jugador_actual}")
        else:
            messagebox.showwarning("Posición ocupada", "Esa casilla ya está ocupada.")

    def VerificarGanador(self):
        combinaciones = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for a,b,c in combinaciones:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] != " ":
                return True
        return False

    def Reiniciar(self):
        self.tablero = [" " for _ in range(9)]
        for boton in self.botones:
            boton.config(text=" ")
        self.jugador_actual = "X"
        self.label_turno.config(text=f"Turno del jugador {self.jugador_actual}")

if __name__ == "__main__":
    root = tk.Tk()
    juego = TicTacToe(root)
    root.mainloop()