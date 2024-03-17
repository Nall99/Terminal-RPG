from time import sleep as delay
import os

# In Home
def HomeMenuDisplay():
    os.system('cls')
    print("--------TERMINAL RPG --------")
    switch = {
        "1": new_game,
        "2": loading,
        "3": guide,
        "4": quit
    }
    print("1 - New Game")
    print("2 - Loading")
    print("3 - Guide")
    print("4 - Quit")
    op = input("Choose an option: ")
    os.system("cls")
    return switch.get(op, default)()

# Home Menu Switch: 
def new_game():
    return 1
def loading():
    return 2
def guide():
    return 3
def quit():
    return 4
def default():
    print("Opção inválida!!!")
    print("Aguarde um pouco e digite novamente uma opção")
    delay(3)
    HomeMenuDisplay()

# In Game
def GameMenuDisplay():
    print("--------TERMINAL RPG --------")
    switch = {
        "1": walk,
        "2": player,
        "3": save_game,
        "4": bestiary,
        "5": guide,
        "6": quit
    }
    print("1 - Walk")
    print("2 - Player")
    print("3 - Save Game")
    print("4 - Bestiary")
    print("5 - Guide")
    print("6 - Quit")
    op = input("Choose an option: ")
    os.system("cls")
    return switch.get(op, default)()
# Game Menu Switch:
def walk():
    return 1
def player():
    pass
def save_game():
    pass
def bestiary():
    pass