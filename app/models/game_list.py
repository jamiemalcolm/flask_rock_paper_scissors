from app.models.game_class import Game
from app.models.player_class import Player

jamie = Player("Jamie", "rock")
laura = Player("Laura", "scissors")
frank = Player("Frank", "paper")


players = [jamie, laura]
game_1 = Game(jamie, laura)

def compare(player_1, player_2):
    if player_1.choice == "rock" and player_2.choice == "scissors":
        return f"{player_1.name} plays {player_1.choice} and {player_2.name} plays {player_2.choice} {player_1.name} wins with {player_1.choice}!"
    if player_1.choice == "paper" and player_2.choice == "rock":
        return f"{player_1.name} plays {player_1.choice} and {player_2.name} plays {player_2.choice} {player_1.choice} wins!"
    if player_1.choice == "scissors" and player_2.choice == "paper":
        return f"{player_1.name} plays {player_1.choice} and {player_2.name} plays {player_2.choice} {player_1.choice} wins!"
    if player_1.choice == player_2.choice:
        return None
    return f"{player_1.name} plays {player_1.choice} and {player_2.name} plays {player_2.choice} {player_2.choice} wins!"


