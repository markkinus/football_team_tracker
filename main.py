# print("welcome")

from player import Player
# from database import connect_db
from database import initialize_db, add_player, get_all_players, update_player, delete_player, search_player, get_top_scorers


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


# # collect player information from user input
# name = input("Enter player name: ")
# position = input("Enter player position: ")

# try:
#     appearances = int(input("Enter number of appearances: "))
#     goals = int(input("Enter number of goals: "))
#     assists = int(input("Enter number of assists: "))

#     # create a new player object with user input
#     player = Player(name, position, appearances, goals, assists)

#     # check if the player information is valid
#     if player.is_valid():
#         # add the player to the database
#         add_player(player)
#     else:
#         print("Invalid player information.")

# except ValueError:
#     print("Invalid input. Please enter valid numbers for appearances, goals, and assists.")

# # retrieve all players from the database
# players = get_all_players()

# # display all players
# if players:
#     print("\nAll Players in the Database:")
#     for player in players:
#         print(f"ID: {player[0]}, Name: {player[1]}, Position: {player[2]}, Appearances: {player[3]}, Goals: {player[4]}, Assists: {player[5]}")
# else:
#     print("No players found in the database.")

# # update player statistics
# print ("\nUpdate Player Statistics:")

# try:
#     player_id = int(input("\nEnter the ID of the player to update: "))
#     new_appearances = int(input("Enter new number of appearances: "))
#     new_goals = int(input("Enter new number of goals: "))
#     new_assists = int(input("Enter new number of assists: "))

#     if new_appearances < 0 or new_goals < 0 or new_assists < 0:
#         print("Invalid input. Appearances, goals, and assists cannot be negative.")
#     else:
#         update_player(player_id, new_appearances, new_goals, new_assists)

# except ValueError:
#     print("Invalid input. Please enter valid numbers for the player statistics.")

# # delete a player
# print("\nDelete Player:")

# try:
#     player_id = int(input("Enter the ID of the player to delete: "))
#     delete_player(player_id)
# except ValueError:
#     print("Invalid input. Please enter a valid player ID.")

# Main function to run the application
def main():
    while True:
        print("\n FOOTBALL TEAM TRACKER ")
        print("1. Add Player")
        print("2. View All Players")
        print("3. Update Player Statistics")
        print("4. Delete Player")
        print("5. Search Player by Name")
        print("6. View Top Scorers")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            print("\nAdd Player:")
            
            name= input("Enter player name: ")
            position= input("Enter player position: ")

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

        elif choice == '2':
            print("\nView All Players:")

            players = get_all_players()

            # display all players
            if players:
                print("\nAll Players in the Database:")
                for player in players:
                    print(f"ID: {player[0]}, Name: {player[1]}, Position: {player[2]}, Appearances: {player[3]}, Goals: {player[4]}, Assists: {player[5]}")
            else:
                print("No players found in the database.")

        elif choice == '3':
            print("\nUpdate Player Statistics:")
            try:
                player_id = int(input("\nEnter the ID of the player to update: "))
                new_appearances = int(input("Enter new number of appearances: "))
                new_goals = int(input("Enter new number of goals: "))
                new_assists = int(input("Enter new number of assists: "))

                if new_appearances < 0 or new_goals < 0 or new_assists < 0:
                    print("Invalid input. Appearances, goals, and assists cannot be negative.")
                else:
                    update_player(player_id, new_appearances, new_goals, new_assists)

            except ValueError:
                print("Invalid input. Please enter valid numbers for the player statistics.")

        elif choice == '4':
            print("\nDelete Player:")

            try:
                player_id = int(input("Enter the ID of the player to delete: "))
                delete_player(player_id)
            except ValueError:
                print("Invalid input. Please enter a valid player ID.")

        elif choice == '5':
            print("\nSearch Player by Name:")
            name = input("Enter the name of the player to search for: ").strip()
            
            if name:
                players = search_player(name)
                
                if players:
                    for player in players:
                        print(f"ID: {player[0]}, Name: {player[1]}, Position: {player[2]}, Appearances: {player[3]}, Goals: {player[4]}, Assists: {player[5]}")
                else:
                    print(f"No players found with name '{name}'.")
            else:
                print("Please enter a valid player name.")

        elif choice == '6':
            print("\nTop Scorers:")
            top_scorers = get_top_scorers()

            if top_scorers:
                for player in top_scorers:
                    print(f" Name: {player[1]},  Goals: {player[4]}")
            else:
                print("No players found in the database.")

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# run the main function if this script is executed directly
if __name__ == "__main__":
    # initialize the database
    initialize_db()
    main()