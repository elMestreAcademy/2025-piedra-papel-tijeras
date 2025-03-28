import random
import sys
import time

import jugadas

cantidad_partidas = 10
auto = True


def muestra_jugadas():
    contador = 0
    for jugada in jugadas.nombre:
        print(f"  - {contador}: ", jugada)
        contador += 1


def introduce_jugada():
    while True:
        selection = input("Elige tu jugada: ").capitalize()
        if selection in jugadas.nombre:
            return selection
        elif selection.isdigit():
            index = int(selection)
            if index < len(jugadas.nombre):
                return jugadas.nombre[index]

        print("Por favor, elige una jugada válida")


def inventarse_jugada(player="El ordenador"):
    print()
    print(f"{player} está pensando una jugada")
    while random.randint(0, 10):
        print(".", end="", flush=True)
        time.sleep(0.2)
    print()

    return random.choice(jugadas.nombre)


def gana(jugada_1, jugada_2):
    index = jugadas.nombre.index(jugada_1)
    return jugada_2 in jugadas.ganadoras[index]


def dibuja(jugada):
    index = jugadas.nombre.index(jugada)
    print(jugadas.frames[index])


def game(auto=False, player_1="player 1", player_2="player 2"):

    muestra_jugadas()
    player_1_move = introduce_jugada() if not auto else inventarse_jugada("Máquina 1")
    player_2_move = inventarse_jugada("Ordenador 2")

    print(f"  · {player_1}:")
    dibuja(player_1_move)
    print(f"  · {player_2}")
    dibuja(player_2_move)

    if player_1_move == player_2_move:
        print("Empate")
        return 0
    elif gana(player_1_move, player_2_move):
        print(f"Victoria de {player_1}")
        return 1
    else:
        print(f"Derrota de {player_1}")
        return -1


def imprimir_ganador(puntuacion):
    print("No hay" if puntuacion == 0 else "El", end=" ")
    print("ganador del juego es", end=" ")
    print("un empate" if puntuacion == 0 else "el jugador" if puntuacion > 0 else "la máquina")


def main():
    partida = 0
    puntuacion = 0
    puntuacion_ganadora = int(cantidad_partidas / 2) + (cantidad_partidas) % 2

    player_1 = "Asqueroso saco de carne" if not auto else "el Ordenador"
    player_2 = "La máquina"

    while partida < cantidad_partidas and abs(puntuacion) < puntuacion_ganadora:
        print()
        print(f"Partida:    {partida} / {cantidad_partidas}")
        print(f"Puntuación: {puntuacion} / {puntuacion_ganadora}")

        puntuacion += game(auto, player_1, player_2)
        partida += 1

    imprimir_ganador(puntuacion)


if __name__ == "__main__":
    main()
