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

# retrieve all players from the database
def get_all_players():
    # connect to the database
    conn = connect_db()
    cursor = conn.cursor()

    # retrieve all players from the database
    cursor.execute('SELECT * FROM players')
    players = cursor.fetchall()

    # close the database connection
    conn.close()

    return players

# search for players by name in the database
def search_player(name):
    # connect to the database
    conn = connect_db()
    cursor = conn.cursor()

    # search for players by name
    cursor.execute('SELECT * FROM players WHERE name LIKE ?', (f'%{name}%',))
    players = cursor.fetchall()

    # close the database connection
    conn.close()

    return players

# update player statistics in the database
def update_player(player_id, appearances, goals, assists):
    # connect to the database
    conn = connect_db()
    cursor = conn.cursor()

    # update player statistics
    cursor.execute(
        '''UPDATE players
           SET appearances = ?, goals = ?, assists = ?
           WHERE id = ?''',
        (appearances, goals, assists, player_id)
    )

    # save the changes to the database
    conn.commit()

    if cursor.rowcount == 0:
        print(f"No player found with ID {player_id}.")
    else:
        print(f"Player {player_id} statistics updated successfully.")

    # close the database connection
    conn.close()

# delete a player from the database
def delete_player(player_id):
    # connect to the database
    conn = connect_db()
    cursor = conn.cursor()

    # delete player from the database
    cursor.execute('DELETE FROM players WHERE id = ?', (player_id,))

    # save the changes to the database
    conn.commit()

    if cursor.rowcount == 0:
        print(f"No player found with ID {player_id}.")
    else:
        print(f"Player {player_id} deleted from the database successfully.")

    # close the database connection
    conn.close()
