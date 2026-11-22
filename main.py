# print("welcome")

from player import Player

# from database import connect_db

# create a new player object with sample data
player1 = Player("Mark", "Mid-fielder", 20, 5, 3)

# check if the player information is valid
if player1.is_valid():
    # display the player's information
    print(player1.display_info())
else:
    print("Invalid player information.")

# connect to the database
# conn = connect_db()

# if conn:
#     print("Connected to the database successfully.")

# conn.close()