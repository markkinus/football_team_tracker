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
menu = st.sidebar.selectbox("Navigation", ["Dashboard", "Add Player", "View All Players"])

# Dashboard page
if menu == "Dashboard":
    st.subheader("Team Overview")

    players = get_all_players()

    col1, col2, col3 = st.columns(3)

    # display metrics for total players, total goals, and total assists
    col1.metric("Total Players", len(players))
    col2.metric("Total Goals", sum(p[4] for p in players))
    col3.metric("Total Assists", sum(p[5] for p in players))