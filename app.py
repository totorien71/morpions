from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/equipes")
def equipes():
    return render_template("equipes.html")

@app.route("/morpion")
def morpion():
    return render_template("morpion.html")

@app.route("/apropos")
def apropos():
    return render_template("apropos.html")

if __name__ == "__main__":
    app.run(debug=True)
