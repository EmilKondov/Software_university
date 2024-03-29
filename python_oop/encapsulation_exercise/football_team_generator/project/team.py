from typing import List, Union
from football_team_generator.project.player import Player

class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"


    def remove_player(self, player_name: str) -> Union[Player, str]: # Union означ
        try:
            player = [p for p in self.__players if p.name == player_name][0]  # чрез тази нула [0], казваме достъпи ми първи елемент в листа.
            self.__players.remove(player)
            return player
        except IndexError:
            return f"Player {player_name} not found"
