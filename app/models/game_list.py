from app.models.game_class import *
from app.models.player_class import Player

jamie = Player("Jamie", "rock")
laura = Player("Laura", "scissors")
frank = Player("Frank", "paper")

game1 = Game(jamie, laura)
game2 = Game(jamie, frank)
game3 = Game(laura, frank)
games = [game1, game2, game3]


# def compare(player_1, player_2):
#         if player_1.choice == "rock" and player_2.choice == "scissors":
#             result = f"{player_1.name} wins! with {player_1.choice}"
#             return f"{player_1.name} plays {player_1.choice} and {player_2.name} plays {player_2.choice} {result}!"
#         if player_1.choice == "paper" and player_2.choice == "rock":
#             result = f"{player_1.name} wins! with {player_1.choice}"
#             return f"{player_1.name} plays {player_1.choice} and {player_2.name} plays {player_2.choice} {result}!"
#         if player_1.choice == "scissors" and player_2.choice == "paper":
#             result = f"{player_1.name} wins! with {player_1.choice}"
#             return f"{player_1.name} plays {player_1.choice} and {player_2.name} plays {player_2.choice} {result}!"
#         if player_1.choice == player_2.choice:
#             return None
#         result = f"{player_2.name} wins! with {player_2.choice}"
#         return f"{player_1.name} plays {player_1.choice} and {player_2.name} plays {result}!"

