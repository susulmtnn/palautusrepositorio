from player import Player
import requests
from player_reader import PlayerReader

class PlayerStats:
        def __init__(self, reader):
            self.player_list = reader.get_players()


        def top_scorers_by_nationality(self, nationality):
            players_nationality=[]

            for player in self.player_list:
                if player.nationality == nationality: 
                    players_nationality.append({
                        "name": player.name,
                        "team": player.team,
                        "goals": player.goals,
                        "assists": player.assists,
                        "total": player.total
                    })

        
            nationality_sorted = sorted(players_nationality, key=lambda player: player["total"], reverse=True)
            final_format=[]
            for player in nationality_sorted:
                final_format.append(f"{player['name']} {player['team']} {player['goals']} + {player['assists']} = {player['total']}")
            return final_format