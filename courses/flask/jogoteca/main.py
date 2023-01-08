from flask import (
    Flask as Flask,
    render_template,
    request,
    redirect,
    session,
    flash
)

from src.includes.game import Game
from src.includes.user import User


APP = Flask(__name__)
APP.secret_key = "jogoteca"

list_games = [
    Game("God of War 2018", "Adventure", "PS5"),
    Game("Tetriz", "Puzzle", "PC"),
    Game("Crash Bandicoot Trilogy", "Platform", "PS5")
]

list_users = [
    User("Davi Guizani", "davigc", "1234")
]


@APP.route("/", methods=["GET"])
def index():
    kwargs = {
        "title_page": "Jogoteca"
    }
    
    return render_template("index.html", **kwargs)


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


@APP.route("/login", methods=["GET"])
def login():
    kwargs = {
        "title_page": "Login"
    }
    
    return render_template("/authentication/login.html", **kwargs)


@APP.route("/login", methods=["POST"])
def verify_login():
    user_login = request.form.get("login").lower().strip()
    user_password = request.form.get("pwd")
    
    logged = False
    
    for user in list_users:
        if user.login == user_login:
            if user.password == user_password:
                logged = True
            break
    
    if logged:
        session["logged_user"] = user_login
        flash(f"`{user_login}` logado com sucesso!")
        return redirect("/games", code=200)
    
    flash("Usuário ou senha incorreta!")
    
    return redirect("/login", code=401)


@APP.route("/logout", methods=["GET"])
def logout():
    if session.get("logged_user"):
        session["logged_user"] = None
        return redirect("/login", code=200)
    
    return redirect("/login", code=401)


if __name__ == "__main__":
    APP.run("127.0.0.1", 5000, True)
