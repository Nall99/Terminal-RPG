from random import randint
import os

def D6():
    return randint(1, 6)

def display(player,max_life_player, enemy, max_life_enemy):

    life_player_percent = player.life / max_life_player
    life_enemy_percent = enemy.life / max_life_enemy

    life_player_asterisk = int(life_player_percent * 20)
    life_enemy_asterisk = int(life_enemy_percent * 20)
    print(f"{enemy.name:-^22}")
    print(f"|{'*' * life_enemy_asterisk:<20}|")
    print("-"*22)
    print(f"{player.nick:-^22}")
    print(f"|{'*' * life_player_asterisk:<20}|")
    print("-"*22)


def initiative(player, enemy):
    ini_player = player.ability + D6()
    ini_enemy = enemy.ability + D6()

    if ini_player >= ini_enemy:
        return [player.nick, enemy.name]
    else:
        return [enemy.name, player.nick]

def player_turn(chosen, player, enemy):
    if chosen == 1: # Player attack
        damage = player.attack() + D6()
        enemy_defense = enemy.defense() + D6()

        if enemy_defense > damage:
            print(f"{enemy.name} dodged his attack")
        elif enemy_defense == damage:
            print(f"{enemy.name} block his attack")
        else:
            damage -= enemy_defense
            print(f"{enemy.name} received {damage} damage")
            enemy.life -= damage
    
    elif chosen == 2: # Player magic attack
        pass
    elif chosen == 3: # Player defense
        pass

def enemy_turn(player, enemy):
    damage = enemy.attack() + D6()
    player_defense = player.defense() + D6()

    if player_defense > damage:
        print(f'{player.nick} dodged enemy attack')
    elif player_defense == damage:
        print(f'{player.nick} blocked enemy attack')
    else:
        damage -= player_defense
        print(f'{player.nick} received {damage} damage')
        player.life -= damage

def finish(player, max_life, enemy):
    if player.life > 0:
        print(f"Congratulations!!!\nYou won {enemy.xp}")
        player.xp += enemy.xp
    else:
        print("You've lost")
        print("Pay 5 coins to get your life back")
        print('-'*20)
        print('1 - Pay')
        print('2 - Not Pay')
        op = int(input('Select an option: '))
        if op == 1:
            player.coins -= 5
            player.life = max_life

    
