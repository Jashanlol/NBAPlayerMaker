from flask import Flask, request, render_template
from .utils.main import get_important_stats, get_nearby_players


app = Flask(__name__)

@app.route("/")
def serveHTML():
    return render_template('nba.html')

@app.route("/myplayer", methods=['POST'])
def generate():
    player_name = request.form["playerName"]
    stats = get_important_stats(player_name)
    if not stats:
        return f"ERROR: player {player_name} was not found!"
    format_stats = '<br/>'.join([f"&emsp;{key}: {round(value, 1)}" for [key, value] in stats.items()])
    return f"<h2>Stats for {player_name.title()}</h2><p>{format_stats}</p>"
