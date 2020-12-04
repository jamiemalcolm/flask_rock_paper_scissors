from app import app 
from flask import render_template
from app.models.game_class import Game
from app.models.game_list import compare
@app.route('/')
def index():
    return render_template('index.html', title ='Home ')

@app.route('/<choice_1>/<choice_2>')
def comparing(choice_1, choice_2):
    return compare(choice_1, choice_2)