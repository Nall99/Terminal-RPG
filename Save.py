import sqlite3
import os
import time

if os.path.exists("data/saves.db") == False:
    conection =  sqlite3.connect("Data/saves.db")
    cursor = conection.cursor() 
    os.system('cls')
    print("Executando")
    time.sleep(3)
    command_sql = """
    CREATE TABLE player_status (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nick TEXT,
        strength INTEGER,
        resistance INTEGER,
        armor INTEGER,
        ability INTEGER,
        power INTEGER,
        life INTEGER,
        mana INTEGER,
        xp INTEGER,
        level INTEGER,
        points INTEGER,
        coins INTEGER
    )
    """
    cursor.execute(command_sql)
    conection.commit()

def saving(status):
    conection =  sqlite3.connect("Data/saves.db")
    cursor = conection.cursor() 

    command_sql = 'INSERT INTO player_status (nick, strength, resistance, armor, ability, power, life, mana, xp, level, points, coins) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

    cursor.execute(command_sql, status)
    conection.commit()

def get_table():
    conection =  sqlite3.connect("Data/saves.db")
    cursor = conection.cursor() 

    command_sql = 'SELECT * FROM player_status'

    cursor.execute(command_sql)
    return cursor.fetchall()