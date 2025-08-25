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

@app.route("/equipes")
def equipes():
    return render_template("equipes.html")


@app.route("/a-propos")
def a_propos():
    return render_template("apropos.html")

@app.route("/morpion")
def morpion():
    return render_template("morpion.html")

if __name__ == "__main__":
     port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

