from dataclasses import dataclass
import os
import Save

@dataclass
class Player:
    id: int = 0
    nick: str = ''
    
    strength: int = 0
    armor: int = 0
    resistance: int = 0
    ability: int = 0
    power: int = 0
    
    life: int = 0
    max_life: int = life
    mana: int = 0
    coins: int = 10


    xp: int = 0
    level: int = 1
    points: int = 7
    inventory: dict = dict

    def level_up(self):
        # Distributing points
        while self.points > 0:
            os.system("cls")
            print(f"{self.nick:-^25}")
            print(f"You has {self.points} points") # Number of free points
            print('-'*25)
            print("Distributed their points")
            print(f"1 - Strength     | {self.strength}")   # Strength points
            print(f"2 - Resistance   | {self.resistance}") # Resistance points
            print(f"3 - Armor        | {self.armor}")      # Armos points
            print(f"4 - Ability      | {self.ability}")    # Ability points
            print(f"5 - Power        | {self.power}")      # Power points
            att = input("Select an attribute: ")
            value = int(input("Enter the value of the attribute: "))
            # Since python doesn't have a switch function, I did 
            # something similar using dict
            switch = {
                "1": self.set_strength,
                "2": self.set_resistance,
                "3": self.set_armor,
                "4": self.set_ability,
                "5": self.set_power 
            }
            try:
                switch.get(att)(value)
                if value > 0:
                    self.points -= value
                elif value < 0:
                    self.points += value
            except TypeError:
                print("ERRO!!!")
                print("Wait a moment and try again...")
                
        
        if self.resistance <= 0:
            self.life = self.mana = 5
        else:
            self.life = self.mana = self.resistance * 5

    if xp in (30, 60, 90, 120, 150, 180, 210, 240, 270, 300):
        level += 1
        level_up()

    def attack(self):
        return self.strength + self.ability
    def defense(self):
        return self.armor + self.ability
    
    def get_inventory(self):
        pass
    def look_status(self):
        os.system("cls")
        print(f"{self.nick:-^20}")
        print(f"Life       | {self.life}")
        print(f"Mana       | {self.mana}")
        print(f"Level      | {self.level}")
        print(f"Coins      | {self.coins}")
        print("-"*20)
        print(f"Strength   | {self.strength}")
        print(f"Armor      | {self.armor}")
        print(f"Ability    | {self.ability}")
        print(f"Power      | {self.power}")
        print(f"Resistance | {self.resistance}")
        print()
    
    def get_id(self):
        return id
    
    def set_strength(self, value):
        self.strength = value
    def get_strength(self):
        return self.strength
    
    def set_armor(self, value):
        self.armor = value
    def get_armor(self, value):
        return self.armor
    
    def set_resistance(self, value):
        self.resistance = value
    def get_resistance(self):
        return self.resistance
    
    def set_ability(self, value):
        self.ability = value
    def get_ability(self):
        return self.ability

    def set_power(self, value):
        self.power = value
    def get_power(self):
        return self.power
