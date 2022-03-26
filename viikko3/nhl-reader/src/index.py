import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists']
        )

        players.append(player)

    print("Oliot:")

    players_fin = filter(
            lambda player: player.nationality == "FIN",
            players
        )
    ordered_by_points = sorted(
        players_fin, 
        key=lambda p: p.get_points(), 
        reverse=True)


    for player in ordered_by_points:
        print(player)

if __name__ == "__main__":
    main()
