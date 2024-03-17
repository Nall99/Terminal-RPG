import sqlite3
from dataclasses import dataclass
from random import choice

@dataclass
class Enemy:
    id: int
    name: str
    
    armor: int
    strength: int
    resistance: int
    ability: int
    power: int

    life: int
    mana: int

    level: float
    xp: int
    
    viewed: bool

    def attack(self):
        return self.strength + self.ability
    def defense(self):
        return self.armor + self.ability

def get_enemy():
    conn = sqlite3.connect("Data/enemys.db")
    cursor = conn.cursor()

    command_sql = 'SELECT * FROM low_level'

    cursor.execute(command_sql)

    return choice(cursor.fetchall())
