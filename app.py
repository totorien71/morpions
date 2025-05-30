from flask import Flask, render_template, request, jsonify
import json
import os
app = Flask(__name__)

DATA_FILE="data/result.json"

@app.route("/")
def accueil():
    return render_template("accueil.html")

@app.route("/news et résultats")
def news_et_résultats():
    return render_template("news et résultats.html")

def read_results():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_results(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
@app.route("/save", methods=["POST"])
def save():
    data = request.json  # {"round": "demi", "match": "semi1", "winner": "Monaco"}
    results = read_results()

    round_name = data.get("round")
    match_id = data.get("match")
    winner = data.get("winner")

    if round_name in results:
        if isinstance(results[round_name], dict):
            results[round_name][match_id] = winner
        else:
            results[round_name] = winner

        if round_name == "finale":
            results["champion"] = winner

        write_results(results)
        return jsonify({"status": "ok", "saved": results})
    return jsonify({"status": "error", "message": "invalid data"}), 400

@app.route("/a-propos")
def a_propos():
    return render_template("apropos.html")

@app.route("/morpion")
def morpion():
    return render_template("morpion.html")

if __name__ == "__main__":
     if not os.path.exists("data"):
        os.mkdir("data")
     if not os.path.exists(DATA_FILE):
        write_results({"quart": {}, "demi": {}, "finale": "", "champion": ""})
     port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

