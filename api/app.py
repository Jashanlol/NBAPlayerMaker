from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def serveHTML():
    return render_template('nba.html')

@app.route("/generate", methods=['POST'])
def generate():
    request_data = request.get_json()
    player_name = request_data.get("playerName")
    
    return player_name