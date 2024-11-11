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
            players_FIN.append(player)


    print("Oliot:")

    for player in players:
        print(player)

    print("\nFinnish Players\n")

    for player in players_FIN:
        print(f"{player.name} {player.team} {player.goals} + {player.assists} = {player.goals + player.assists}")


if __name__ == "__main__":
    main()