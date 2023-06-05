from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def serveHTML():
    return render_template('nba.html')

@app.route("/myplayer", methods=['POST'])
def generate():
    player_name = request.form["playerName"]
    return f"Generating player... {player_name}"