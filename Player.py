from dataclasses import dataclass

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

    def attack(self):
        pass
    def defense(self):
        pass
    def see_inventory(self):
        pass
    def see_attribute(self):
        pass
    
    def set_attribute(self):
         while self.points > 0:
            print(f"{self.nick:-^25}")
            print(f"You has {self.points} points")
            print('-'*25)
            print("distributed their points")
            print("1 - Strength")
            print("2 - Resistance")
            print("3 - Armor")
            print("4 - Ability")
            print("5 - Power")
            att = int(input("Select an attribute: "))
            value = int(input("Enter the value of the attribute: "))
    
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