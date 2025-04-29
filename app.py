from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "motdepasse_secret"  # Ne change pas

@app.route("/")
def accueil():
    return render_template("accueil.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/a-propos")
def a_propos():
    return render_template("a_propos.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        mot_de_passe = request.form.get("motdepasse")
        if mot_de_passe == "1234":  # Change ici ton mot de passe si tu veux
            session["autorise"] = True
            return redirect(url_for("morpion"))
    return render_template("login.html")

@app.route("/morpion")
def morpion():
    if not session.get("autorise"):
        return redirect(url_for("login"))
    return render_template("morpion.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("accueil"))

if __name__ == "__main__":
    app.run(debug=True)