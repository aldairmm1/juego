import random

# Definimos una función para crear una nueva baraja
def crear_baraja():
    return ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

def valor_carta(carta):
    if carta in ['J', 'Q', 'K']:
        return 10
    elif carta == 'A':
        return 11  # El As puede valer 11 o 1, 
    else:
        return int(carta)

def ajustar_valor_as(mano):
    # Ajusta el valor del As en la mano si el total es mayor a 21
    while sum(valor_carta(carta) for carta in mano) > 21 and 'A' in mano:
        mano[mano.index('A')] = '1'  # Cambia el valor de 'A' a '1'
    return mano

def jugar_blackjack():
    print("¡Bienvenido al juego de Blackjack!")

    # Crear y barajar una nueva baraja para cada partida
    baraja_blackjack = crear_baraja()
    random.shuffle(baraja_blackjack)

    # Iniciar las manos del jugador y del crupier
    mano_jugador = []
    mano_crupier = []

    # Repartir dos cartas a cada jugador
    for _ in range(2):
        mano_jugador.append(baraja_blackjack.pop())
        mano_crupier.append(baraja_blackjack.pop())

    # Mostrar la mano del jugador y una carta del crupier
    print("Tu mano:", mano_jugador)
    print("Carta del crupier:", mano_crupier[0])

    # Turno del jugador
    while True:
        mano_jugador = ajustar_valor_as(mano_jugador)
        total_jugador = sum(valor_carta(carta) for carta in mano_jugador)
        if total_jugador > 21:
            print("Te has pasado de 21. ¡Has perdido!")
            return -1

        opcion = input("¿Quieres pedir otra carta (p) o plantarte (s)? ").strip().lower()
        if opcion == 'p':
            carta_nueva = baraja_blackjack.pop()
            mano_jugador.append(carta_nueva)
            print("Has recibido:", carta_nueva)
            print("Tu mano actual:", mano_jugador)
        elif opcion == 's':
            break
        else:
            print("Opción no válida. Por favor, elige 'p' para pedir carta o 's' para plantarte.")

    # Turno del crupier
    while sum(valor_carta(carta) for carta in mano_crupier) < 17:
        carta_nueva_crupier = baraja_blackjack.pop()
        mano_crupier.append(carta_nueva_crupier)
        mano_crupier = ajustar_valor_as(mano_crupier)

    # Mostrar manos finales
    print("Tu mano:", mano_jugador)
    print("Mano del crupier:", mano_crupier)

    # Determinar ganador
    total_jugador = sum(valor_carta(carta) for carta in mano_jugador)
    total_crupier = sum(valor_carta(carta) for carta in mano_crupier)
    if total_jugador > 21 or (total_crupier <= 21 and total_crupier > total_jugador):
        print("¡El crupier gana!")
        return -1
    elif total_jugador == total_crupier:
        print("Es un empate.")
        return 0
    else:
        print("¡Felicidades! ¡Has ganado!")
        return 1

# Jugar una partida
resultado = jugar_blackjack()
