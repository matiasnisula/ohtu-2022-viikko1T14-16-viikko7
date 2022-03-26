

class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists

    def get_points(self):
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} team {self.team} goals {str(self.goals):2} assists {self.assists}"
