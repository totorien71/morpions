from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("accueil.html")

@app.route("/news et résultats")
def contact():
    return render_template("contact.html")

@app.route("/apropos")
def a_propos():
    return render_template("apropos.html")

@app.route("/morpion")
def morpion():
    return render_template("morpion.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

