from Saves import db
from dataclasses import dataclass
from time import sleep as delay
import os

@dataclass
class Player:
    nick: str
    
    strength: int = 0
    armor: int = 0
    resistance: int = 0
    ability: int = 0
    power: int = 0
    
    life: int = 0
    mana: int = 0

    xp: int = 0
    level: int = 1
    points: int = 7
    inventory: dict = dict

    if os.path.exists("Saves/saves.db") == False:
        db.first_save()
        print("criando save...")
        delay(5)

    def attack(self):
        pass
    def defense(self):
        pass
    def get_inventory(self):
        pass
    def get_attribute(self):
        pass
    
    def set_attribute(self):
        while self.points > 0:
            os.system("cls")
            print(f"{self.nick:-^25}")
            print(f"You has {self.points} points")
            print('-'*25)
            print("distributed their points")
            print("1 - Strength")
            print("2 - Resistance")
            print("3 - Armor")
            print("4 - Ability")
            print("5 - Power")
            att = input("Select an attribute: ")
            value = int(input("Enter the value of the attribute: "))
            switch = {
                "1": self.set_strength,
                "2": self.set_resistance,
                "3": self.set_armor,
                "4": self.set_ability,
                "5": self.set_power 
            }
            try:
                switch.get(att)(value)
                self.points -= value
            except TypeError:
                print("ERRO!!!")
                print("Wait a moment and try again...")
                delay(3)
        db.saving((self.nick, 
                   self.strength, 
                   self.resistance, 
                   self.armor, 
                   self.ability, 
                   self.power, 
                   self.life, 
                   self.mana, 
                   self.xp, 
                   self.level, 
                   self.points))

    
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