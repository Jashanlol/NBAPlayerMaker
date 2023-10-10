from flask import Flask, request, render_template
from utils.main import get_important_stats, get_nearby_players


app = Flask(__name__)

@app.route("/")
def serveHTML():
    return render_template('nba.html')

@app.route("/myplayer", methods=['POST'])
def generate():
    player_name = request.form["playerName"]
    return get_important_stats(player_name)
