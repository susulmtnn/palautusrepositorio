
from player import Player
import requests

class PlayerReader:
    def __init__(self, address):
        self.url = address
        
    def get_players(self):
        response=requests.get(self.url).json()
        print(response)

        players_dicti = []

        for player_dict in response:
            player = Player(player_dict)
            players_dicti.append(player)
        return players_dicti
