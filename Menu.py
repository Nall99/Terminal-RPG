from time import sleep as delay
from Player import Player
import os
def exibir():
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
    return switch.get(op, default)()

def new_game():
    os.system("cls")
    nick = input("Digite seu Nick:\n")
    pl = Player(nick)
    pl.set_attribute()



def loading():
    pass
def guide():
    pass
def quit():
    pass
def default():
    print("Opção inválida!!!")
    print("Aguarde um pouco e digite novamente uma opção")
    delay(3)
    return -1