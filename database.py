import sqlite3

# connect to the database
def connect_db():
    conn = sqlite3.connect('football.db')
    return conn

# insert a new player into the database
def add_player_to_db(player):
    