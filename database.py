import sqlite3

# connect to the database
def connect_db():
    conn = sqlite3.connect('football.db')
    return conn

# insert a new player into the database
def add_player(player):

    # connect to the database
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        '''INSERT INTO players (name, position, appearances, goals, assists)
                      VALUES (?, ?, ?, ?, ?)''',
                   (
                       player.name, 
                       player.position, 
                       player.appearances, 
                       player.goals, 
                       player.assists
                    ))
    # save the changes to the database
    conn.commit()

    # close the database connection
    conn.close()

    print(f"Player {player.name} added to the database successfully.")
    