class Player:
    # constructor to initialize player attributes
    def __init__(self, name, position, appearances, goals, assists):
        # store player's information as object attributes
        self.name = name
        self.position = position
        self.appearances = appearances
        self.goals = goals
        self.assists = assists

    # method to validate player information
    def is_valid(self):

        # check that name and postion are not empty and that appearances, goals, and assists are non-negative
        return (
            self.name.strip() != "" and
            self.position.strip() != "" and
            self.appearances >= 0 and
            self.goals >= 0 and
            self.assists >= 0
        )

    
    # # method to update player statistics
    # def update_stats(self, appearances, goals, assists):

    #     # assign new values to the player's statistics
    #     self.appearances == appearances
    #     self.goals == goals
    #     self.assists == assists

    # # method to display player information
    # def display_info(self):

    #     return (
    #         f"Name: {self.name}\n"
    #         f"Position: {self.position}\n"
    #         f"Appearances: {self.appearances}\n"
    #         f"Goals: {self.goals}\n"
    #         f"Assists: {self.assists}"
    #     )