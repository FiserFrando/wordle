from src.words import palabras
from random import choice
from color_letters import Color

pick = choice(palabras)
intentos = 0

while True:
    palabra = input("\n\nIngresa una palabra de 5 letras: ")

    if palabra == pick:
        intentos += 1
        for i in palabra:
            print(Color.GREEN.value + i + Color.RESET.value, end=' ')

        print(f'\n\nResolviste el puzzle en {intentos} intentos!')
        break

    for i in range(5):
        if palabra[i] == pick[i]:
            print(Color.GREEN.value + f'{palabra[i]}' + Color.RESET.value, end=' ')
        elif palabra[i] in pick:
            print(Color.YELLOW.value + f'{palabra[i]}' + Color.RESET.value, end=' ')
        else:
            print(Color.WHITE.value + f'{palabra[i]}' + Color.RESET.value, end=' ')

    intentos += 1

    if intentos > 5:
        break
