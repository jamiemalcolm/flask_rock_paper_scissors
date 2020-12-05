from app import app 
from flask import render_template
from app.models.game_class import Game
from app.models.game_list import *
@app.route('/')
def index():
    return render_template('index.html', title ='Home ')

@app.route('/<player_1>/<choice_1>/<player_2>/<choice_2>')
def comparing(player_1, player_2, choice_1, choice_2):
    player_1 = Player(player_1, choice_1)
    player_2 = Player(player_2, choice_2)
    return compare(player_1, player_2)