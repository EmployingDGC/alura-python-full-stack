from flask import (
    Flask as Flask,
    render_template,
    request,
    redirect
)

from src.includes.game import Game


APP = Flask(__name__)    

list_games = [
    Game("God of War 2018", "Adventure", "PS5"),
    Game("Tetriz", "Puzzle", "PC"),
    Game("Crash Bandicoot Trilogy", "Platform", "PS5")
]


@APP.route("/", methods=["GET"])
def index():
    kwargs_index = {
        "title_page": "Jogoteca"
    }
    
    return render_template("index.html", **kwargs_index)


@APP.route("/games", methods=["GET"])
def games():
    kwargs = {
        "title_header": "Jogos",
        "title_page": "Jogos",
        "games": list_games
    }
    
    return render_template("/games/games.html", **kwargs)


@APP.route("/games/new", methods=["GET"])
def games_new():
    kwargs = {
        "title_page": "Novo Jogo"
    }
    
    return render_template("/games/new.html", **kwargs)


@APP.route("/games/new", methods=["POST"])
def add_new_game():
    game_name = request.form.get("game_name")
    game_category = request.form.get("game_category")
    game_platform = request.form.get("game_platform")

    game = Game(game_name, game_category, game_platform)
    
    list_games.append(game)
    
    return redirect("/games", code=200)


if __name__ == "__main__":
    APP.run("127.0.0.1", 5000, True)
