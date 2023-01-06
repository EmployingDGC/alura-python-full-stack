from flask import (
    Flask as Flask,
    render_template as render_template
)

from src.includes.game import Game
from src.includes.utils.string import clean_render_template

APP = Flask(__name__)    

list_games = [
    Game("God of War 2018", "Adventure", "PS5"),
    Game("Tetriz", "Puzzle", "PC"),
    Game("Crash Bandicoot Trilogy", "Platform", "PS5")
]


@APP.route("/", methods=["GET"])
def index():
    kwargs_index = {
        "title_page": "Jogoteca",
        "body_render": "<h1>Bem Vindo a nossa Jogoteca</h1>"
    }
    
    page = render_template("index.html", **kwargs_index)
    
    return clean_render_template(page)


@APP.route("/games", methods=["GET"])
def games():
    kwargs_games = {
        "title_header": "Jogos",
        "games": list_games
    }
    
    kwargs_index = {
        "title_page": "Jogos",
        "body_render": render_template("/games/index.html", **kwargs_games)
    }
    
    page = render_template("index.html", **kwargs_index)
    
    return clean_render_template(page)


@APP.route("/games/new", methods=["GET"])
def games_new():
    kwargs_new = {}
    
    kwargs_index = {
        "title_page": "Novo Jogo",
        "body_render": render_template("/games/new.html", **kwargs_new)
    }
    
    page = render_template("index.html", **kwargs_index)
    
    return clean_render_template(page)


if __name__ == "__main__":
    APP.run("127.0.0.1", 5000, True)
