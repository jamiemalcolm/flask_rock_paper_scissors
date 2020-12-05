class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.result = []


    def compare(self, player_1, player_2):
        if player_1.choice == "rock" and player_2.choice == "scissors":
            result = f"{player_1.name} wins! with {player_1.choice}"
            return f"{player_1.name} plays {player_1.choice} and {player_2.name} plays {player_2.choice} {result}!"
        if player_1.choice == "paper" and player_2.choice == "rock":
            result = f"{player_1.name} wins! with {player_1.choice}"
            return f"{player_1.name} plays {player_1.choice} and {player_2.name} plays {player_2.choice} {result}!"
        if player_1.choice == "scissors" and player_2.choice == "paper":
            result = f"{player_1.name} wins! with {player_1.choice}"
            return f"{player_1.name} plays {player_1.choice} and {player_2.name} plays {player_2.choice} {result}!"
        if player_1.choice == player_2.choice:
            return None
        result = f"{player_2.name} wins! with {player_2.choice}"
        return f"{player_1.name} plays {player_1.choice} and {player_2.name} plays {result}!"

    def add_result(self, game):
        self.result.append(self.compare(game.player_1, game.player_2))