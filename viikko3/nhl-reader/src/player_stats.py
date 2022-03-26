
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players_by_nat = filter(
            lambda player: player.nationality == nationality,
            self.players
        )
        ordered_by_points = sorted(
            players_by_nat, 
            key=lambda p: p.get_points(), 
            reverse=True)

        return ordered_by_points