import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats=StatisticsService(PlayerReaderStub())

    def test_konstruktori_saa_olion(self):
        expected_players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
        for i in range(len(expected_players)-1):
            self.assertEqual(self.stats._players[i].name, expected_players[i].name)

    def test_if_name_in_player_name_return_name(self):

        self.assertEqual(self.stats.search("Kurri"), self.stats._players[2])

    def test_if_name_not_in_player_return_none(self):
        self.assertEqual(self.stats.search("Nikke"), None)

    def test_team(self):
        expected_players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

        self.assertAlmostEqual(len(self.stats.team("PIT")), 1)

    def test_top(self):
        self.assertEqual(len(self.stats.top(2)), 2)