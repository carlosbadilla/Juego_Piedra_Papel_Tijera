import random

def jugar():
    opciones = ['Piedra', 'Papel', 'Tijeras']

    while True:
        computadora = random.choice(opciones)
        print("\nElige una opción:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijeras")
        print("4. Salir")

        jugador = input("¿Qué eliges? (1/2/3/4): ")

        if jugador == '4':
            print("\n¡Hasta luego!")
            break
        elif jugador in ['1', '2', '3']:
            jugador = opciones[int(jugador) - 1]
            print("\nTú eliges:", jugador)
            print("La computadora elige:", computadora)
            resultado = determinar_ganador(jugador, computadora)
            print(resultado)
        else:
            print("\nOpción inválida. Por favor, elige una opción válida.")

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "¡Empate!"
    elif (jugador == 'Piedra' and computadora == 'Tijeras') or \
         (jugador == 'Papel' and computadora == 'Piedra') or \
         (jugador == 'Tijeras' and computadora == 'Papel'):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"

if __name__ == "__main__":
    print("Bienvenido a Piedra, Papel o Tijeras")
    jugar()
