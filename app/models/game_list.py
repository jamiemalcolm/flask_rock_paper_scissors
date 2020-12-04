from app.models.game_class import Game
from app.models.player_class import Player

jamie = Player("Jamie", "rock")
laura = Player("Laura", "scissors")

game_1 = Game(jamie, laura)




def compare(choice_1, choice_2):
    if choice_1 == "rock" and choice_2 == "scissors":
        return f"{choice_1} wins!"
    if choice_1 == "paper" and choice_2 == "rock":
        return f"{choice_1} wins!"
    if choice_1 == "scissors" and choice_2 == "paper":
        return f"{choice_1} wins!"
    return f"{choice_2} wins!"