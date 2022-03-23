import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_player_if_exits(self):
        player = self.statistics.search("Kurri")

        self.assertEqual(player.name, "Kurri")

    def test_search_returns_none_if_player_doesnt_exits(self):
        player = self.statistics.search("Litmanen")

        self.assertEqual(player, None)

    def test_team_returns_correct_players(self):
        team = self.statistics.team("EDM")
        player_list = ["Semenko", "Kurri", "Gretzky"]

        for player in team:
            if player.name in player_list:
                player_list.remove(player.name)

        self.assertEqual(len(player_list), 0)

    def test_top_scorers_returns_players_in_correct_order(self):
        top_5 = self.statistics.top_scorers(5)
        correct_top_5 = ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]
        correct_order = True

        for i in range(len(top_5)):
            if correct_top_5[i] != top_5[i].name:
                correct_order = False

        self.assertEqual(correct_order, True)