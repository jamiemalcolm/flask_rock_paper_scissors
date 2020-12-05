from app import app 
from flask import render_template, request
from app.models.game_class import Game
from app.models.game_list import *
@app.route('/')
def index():
    return render_template('index.html', title ='Home ')


@app.route('/<player_1>/<choice_1>/<player_2>/<choice_2>')
def comparing(player_1, player_2, choice_1, choice_2,):
    player_1 = Player(player_1, choice_1)
    player_2 = Player(player_2, choice_2)
    game = Game(player_1, player_2)
    games.append(game)
    game.compare(player_1, player_2)
    return render_template('results.html', title ='Results ', games = games)

@app.route('/play')
def result():
    return render_template('play.html', title ='Results ', games = games)

@app.route('/play', methods =['POST', 'GET'])
def play():
    player_1_name = request.form["name"]
    player_1_choice = request.form["choice"]
    player_2_name = request.form["name_2"]
    player_2_choice = request.form["choice_2"]
    player_1 = Player(player_1_name, player_1_choice)
    player_2 = Player(player_2_name, player_2_choice)
    game = Game(player_1, player_2)
    game.compare(player_1, player_2)
    games.append(game)
    return render_template('play.html', title ='Play', games = games)

@app.route('/results')
def results():
    return render_template('results', titel ='Results ', games = games)