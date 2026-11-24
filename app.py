import streamlit as st

from database import initialize_db, add_player, get_all_players, update_player, delete_player, search_player, get_top_scorers, export_players_to_csv

from player import Player

# Initialize the database
initialize_db()

# page configuration
st.set_page_config(page_title="Football Team Tracker", layout="wide")

# Main title and description
st.title("Football Team Tracker")
st.write("Manage your football team players and their statistics.")

# Sidebar navigation
menu = st.sidebar.selectbox("Navigation", ["Dashboard", "Add Player", "View All Players", "Search Players"])

# Dashboard page
if menu == "Dashboard":
    st.subheader("Team Overview")

    players = get_all_players()

    col1, col2, col3 = st.columns(3)

    # display metrics for total players, total goals, and total assists
    col1.metric("Total Players", len(players))
    col2.metric("Total Goals", sum(p[4] for p in players))
    col3.metric("Total Assists", sum(p[5] for p in players))

# Add Player page
elif menu == "Add Player":
    st.subheader("Add New Player")

    # collect player information from user input
    name = st.text_input("Player Name")
    position = st.text_input("Position")

    appearances = st.number_input(
        "Appearances", min_value=0, step=1
    )
    
    goals = st.number_input("Goals", min_value=0, step=1)
    assists = st.number_input("Assists", min_value=0, step=1)

    # add player button
    if st.button("Add Player"):
        player = Player(name, position, appearances, goals, assists)

        # validate player information before adding to the database
        if player.is_valid():
            add_player(player)
            st.success(f"Player {player.name} added successfully!")
        else: 
            st.error("Invalid player information. Please check the inputs.")

# View All Players page
elif menu == "View All Players":
    st.subheader("All Players")

    players = get_all_players()

    # display all players in the database
    if players:
        for player in players:
            st.write(f"ID: {player[0]}, Name: {player[1]}, Position: {player[2]}, Appearances: {player[3]}, Goals: {player[4]}, Assists: {player[5]}")
    else:
        st.info("No players found in the database.")

elif menu == "Search Players":
    st.subheader("Search Players by Name")

    search_name = st.text_input("Enter player name to search")

    # search button
    if st.button("Search"):
        results = search_player(search_name)

        # display search results
        if results:
            for player in results:
                st.write(f"ID: {player[0]}, Name: {player[1]}, Position: {player[2]}, Appearances: {player[3]}, Goals: {player[4]}, Assists: {player[5]}")
        else:
            st.info("No players found with that name.")