class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player_1_score = 0
        self.player_2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player_1_score = self.player_1_score + 1
        else:
            self.player_2_score = self.player_2_score + 1

    def check_winner(self):
        point_difference = self.player_1_score - self.player_2_score
        if point_difference == 1:
            return "Advantage player1"
        elif point_difference == -1:
            return  "Advantage player2"
        elif point_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
    
    def check_draw(self):
        if self.player_1_score == 0:
            return "Love-All"
        elif self.player_1_score == 1:
            return "Fifteen-All"
        elif self.player_1_score == 2:
            return "Thirty-All"
        elif self.player_1_score == 3:
            return "Forty-All"
        else:
            return "Deuce"

    def check_score(self, points):
        if points == 0:
            return "Love"
        elif points == 1:
            return "Fifteen"
        elif points == 2:
            return "Thirty"
        elif points == 3:
            return "Forty"

    def get_score(self):
        if self.player_1_score == self.player_2_score:
            score = self.check_draw()
        elif self.player_1_score >= 4 or self.player_2_score >= 4:
            score = self.check_winner()
        else:
            player_1_score = self.check_score(self.player_1_score)
            player_2_score = self.check_score(self.player_2_score)
            score = f"{player_1_score}-{player_2_score}"

        return score
