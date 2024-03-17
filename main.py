# Libraries
from time import sleep as delay
import Save
import Enemy
import os
import Menu
import Combat
from Player import Player

# Player Class
pl = Player()

def save_status():
    Save.saving(( 
                    pl.nick, 
                    pl.strength, 
                    pl.resistance, 
                    pl.armor, 
                    pl.ability, 
                    pl.power, 
                    pl.life, 
                    pl.mana, 
                    pl.xp, 
                    pl.level, 
                    pl.points,
                    pl.coins
                ))
def load_status():
    player_saves = []
    results = Save.get_table()
    for result in results:
        id, nick, strength, resistance, armor, ability, power, life, mana, xp, level, points, coins = result
        player_save = Player(id,
                             nick, 
                             strength, 
                             resistance, 
                             armor,
                             ability,
                             power,
                             life,
                             mana,
                             coins,
                             xp,
                             level,
                             points
                             )
        player_saves.append(player_save)
    return player_saves
def load_enemy():
    id, name, streng, resistance, armor, ability, power, life, mana, level, xp, viewed = Enemy.get_enemy()
    chosen_enemy = Enemy.Enemy(id,
                     name,
                     armor,
                     streng,
                     resistance,
                     ability,
                     power,
                     life,
                     mana,
                     level,
                     xp,
                     viewed)
    return chosen_enemy


# Initial Menu State
choose_IniMenu = Menu.HomeMenuDisplay() # Takes the user's decision
while True:
    os.system("cls") # Clean Terminal
    if  choose_IniMenu == 1:  # New Game
        # Get user nickname
        print("What's your nickname?")
        pl.nick = input()

        # Distributing points
        while pl.points > 0:
            os.system("cls")
            print(f"{pl.nick:-^25}")
            print(f"You has {pl.points} points") # Number of free points
            print('-'*25)
            print("Distributed their points")
            print(f"1 - Strength     | {pl.strength}")   # Strength points
            print(f"2 - Resistance   | {pl.resistance}") # Resistance points
            print(f"3 - Armor        | {pl.armor}")      # Armos points
            print(f"4 - Ability      | {pl.ability}")    # Ability points
            print(f"5 - Power        | {pl.power}")      # Power points
            att = input("Select an attribute: ")
            value = int(input("Enter the value of the attribute: "))
            # Since python doesn't have a switch function, I did 
            # something similar using dict
            switch = {
                "1": pl.set_strength,
                "2": pl.set_resistance,
                "3": pl.set_armor,
                "4": pl.set_ability,
                "5": pl.set_power 
            }
            try:
                switch.get(att)(value)
                if value > 0:
                    pl.points -= value
                elif value < 0:
                    pl.points += value
            except TypeError:
                print("ERRO!!!")
                print("Wait a moment and try again...")
                delay(3)
        
        if pl.resistance <= 0:
            pl.life = pl.mana = 5
        else:
            pl.life = pl.mana = pl.resistance * 5

        save_status()
        break
    elif choose_IniMenu == 2: # Load Game
        saves = load_status()
        for save in saves:
            print(f"{save.id} - {save.nick:<10} | LEVEL: {save.level}")
        op = int(input("Choose your save: "))-1
        pl: Player = saves[op]
        pl.look_status()
        confirm = input("Continue[Y/N]: ").lower()
        if confirm == 'y':
            break
        else:
            continue
    elif choose_IniMenu == 4: # Quit Game
        break

os.system("cls") # Clean Terminal
# Game Menu State
chooseGameMenu = Menu.GameMenuDisplay()
while True:
    if chooseGameMenu == 1:
        en = load_enemy()
        print(f"{'Walking':-^20}")
        print(f"You find a {en.name}")
        print("-"*20)
        print("1 - Fight")
        print("2 - Run")
        print("3 - Back to Game Menu")
        op = int(input("Select an option: "))
        
        if op == 1:
            turns = Combat.initiative(pl, en)
            
            max_life_player = pl.life
            max_life_enemy = en.life
            
            while en.life > 0 and pl.life > 0:
                os.system("cls")
                Combat.display(pl, max_life_player, en, max_life_enemy)
                if turns[0] == pl.nick:
                    
                    print("1 - attack")
                    print("2 - magic")
                    print("3 - defense")
                    print("4 - run")
                    opFight = int(input("Select an option: "))
                    print("-"*22)
                    Combat.player_turn(opFight, pl, en)
                
                elif turns[0] == en.name:
                    Combat.enemy_turn(pl, en)
                
                turns.append(turns.pop(0))
                delay(1)
            os.system("cls")
            Combat.finish(pl, max_life_player, en)
                    

