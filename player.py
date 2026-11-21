class Player:
    def __init__(self, name, position, appearances, goals, assists):
        self.name = name
        self.position = position
        self.appearances = appearances
        self.goals = goals
        self.assists = assists

    def is_valid(self):
        return (
            self.name.strip() != "" and
            self.position.strip() != "" and
            self.appearances >= 0 and
            self.goals >= 0 and
            self.assists >= 0
        )