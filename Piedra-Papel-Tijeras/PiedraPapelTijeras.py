import random

jugada=int(input("Selecciona:\n1-Piedra\n2-Papel\n3-Tijeras\n"))

if jugada==1:
    match random.randint(1, 3):
        case 1:
            print("-Piedra-")
            print("Empate")
        case 2:
            print("-Papel")
            print("Perdiste")
        case 3:
            print("-Tijeras-")
            print("Ganaste")
if jugada == 2:
    match random.randint(1, 3):
        case 1:
            print("-Piedra-")
            print("Ganaste")
        case 2:
            print("-Papel-")
            print("Empate")
        case 3:
            print("-Tijeras-")
            print("Perdiste")
if jugada == 3:
    match random.randint(1, 3):
        case 1:
            print("-Piedra-")
            print("Perdiste")
        case 2:
            print("-Papel-")
            print("Ganaste")
        case 3:
            print("-Tijeras-")
            print("Empate")