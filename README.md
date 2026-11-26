# Football Team Tracker

A Python-based application for managing football players and tracking their performance statistics. The system provides a command-line interface and a Streamlit web interface, with SQLite for persistent data storage.

## 1. Project Overview

Football Team Tracker is designed to make it easier to manage football team records. It allows users to register players, maintain their statistics, search for player records and identify top goal scorers.

## 2. Problem Statement

Managing football player information manually can become difficult as the number of players increases. Records can be misplaced, updating statistics can be inconvenient, and identifying top-performing players may require manually reviewing records.

## 3. Proposed Solution

Football Team Tracker provides a simple digital system for storing and managing player information. It uses Python for application logic, SQLite for data storage and Streamlit for a user-friendly interface.

## 4. Features

- **Add Players:** Register players with their names, positions and statistics.
- **View Players:** Display all registered players.
- **Update Statistics:** Modify player appearances, goals and assists.
- **Delete Players:** Remove player records.
- **Search Players:** Find players using their names, including partial-name searches.
- **Top Scorers:** Display players ranked by goals.
- **Dashboard:** View total players, goals and assists.
- **CSV Export:** Download player records as a CSV file.
- **Input Validation:** Validate player information before saving records.

## 5. Technologies Used

 Python | Main programming language 
 SQLite | Persistent database storage 
 Streamlit | Web interface 
 Pandas | Preparing player records for CSV export 
 CSV | Exporting player data 
 Git & GitHub | Version control and project hosting 

## 6. Project Structure

```text
football_team_tracker/
│
├── app.py
├── main.py
├── player.py
├── database.py
├── football.db
├── requirements.txt
├── .gitignore
├── README.md
```


## 7. Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git
- A code editor such as Visual Studio Code

### Step 1: Clone the repository

```bash
git clone https://github.com/markkinus/football_team_tracker.git
```

### Step 2: Navigate into the project folder

```bash
cd football_team_tracker
```

### Step 3: Create a virtual environment

```bash
python -m venv .venv
```

### Step 4: Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

## 8. Running the Application

### Streamlit Web Application

```bash
streamlit run app.py
```

### Command-Line Application

```bash
python main.py
```

## 9. Database

The application uses SQLite to store player records.

The `players` table contains:

- `id` – Unique player identifier
- `name` – Player name
- `position` – Playing position
- `appearances` – Number of appearances
- `goals` – Number of goals scored
- `assists` – Number of assists

Data is stored persistently in the local SQLite database.

## 10. Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Make your changes.
4. Commit your changes.
5. Submit a pull request.

## 11. License

This project is licensed under the [MIT License](LICENSE).