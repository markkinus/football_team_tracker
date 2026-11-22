# print("welcome")

from player import Player
# from database import connect_db
from database import add_player, get_all_players


# # create a new player object with sample data
# player1 = Player("Mark", "Mid-fielder", 20, 5, 3)

# # check if the player information is valid
# if player1.is_valid():
#     # display the player's information
#     print(player1.display_info())
# else:
#     print("Invalid player information.")

# connect
# conn = connect_db()

# if conn:
#     print("Connected to the database successfully.")

# conn.close()


# collect player information from user input
name = input("Enter player name: ")
position = input("Enter player position: ")

try:
    appearances = int(input("Enter number of appearances: "))
    goals = int(input("Enter number of goals: "))
    assists = int(input("Enter number of assists: "))

    # create a new player object with user input
    player = Player(name, position, appearances, goals, assists)

    # check if the player information is valid
    if player.is_valid():
        # add the player to the database
        add_player(player)
    else:
        print("Invalid player information.")

except ValueError:
    print("Invalid input. Please enter valid numbers for appearances, goals, and assists.")

# retrieve all players from the database
players = get_all_players()

# display all players
if players:
    print("\nAll Players in the Database:")
    for player in players:
        print(f"ID: {player[0]}, Name: {player[1]}, Position: {player[2]}, Appearances: {player[3]}, Goals: {player[4]}, Assists: {player[5]}")
else:
    print("No players found in the database.")