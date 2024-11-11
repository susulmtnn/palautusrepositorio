import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []
    players_FIN=[]

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

        if player.nationality=='FIN':
            players_FIN.append({"name": player.name, "team":player.team, "goals": player.goals, "assists": player.assists, "total":player.total})
        finnish_sorted=sorted(players_FIN, key=lambda player: player["total"], reverse=True)


    print("Oliot:")

    for player in players:
        print(player)

    print("\nFinnish Players\n")

    for player in finnish_sorted:
        print(f"{player['name']} {player['team']} {player['goals']} + {player['assists']} = {player['total']}")


if __name__ == "__main__":
    main()