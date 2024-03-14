import sqlite3
import os

conection =  sqlite3.connect("Saves/saves.db")
cursor = conection.cursor()

if os.path.exists("Saves/saves.db") == False:
    command_sql = """
    CREATE TABLE players (
        id INTERGER PRIMARY KEY,
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
        points INTEGER
    )
    """
    cursor.execute(command_sql)
    conection.commit()

def saving(status):
    global cursor
    global conection

    command_sql = 'INSERT INTO players (nick, strength, resistance, armor, ability, power, life, mana, xp, level, points) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

    cursor.execute(command_sql, status)
    conection.commit()    