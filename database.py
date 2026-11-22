import sqlite3

# connect to the database
def connect_db():
    conn = sqlite3.connect('football.db')
    return conn