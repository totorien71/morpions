from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "motdepasse_secret"  # Obligatoire pour utiliser les sessions

# Page d'accueil (publique)
@app.route("/")
def accueil():
    return render_template("accueil.html")

# Page de contact (publique)
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Page à propos (publique)
@app.route("/a-propos")
def a_propos():
    return render_template("a_propos.html")

# Page de connexion (publique)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        mot_de_passe = request.form.get("motdepasse")
        if mot_de_passe == "1234":  # Tu peux changer le mot de passe ici
            session["autorise"] = True
            return redirect(url_for("morpion"))
    return render_template("login.html")

# Page morpion (protégée)
@app.route("/morpion")
def morpion():
    if not session.get("autorise"):
        return redirect(url_for("login"))
    return render_template("morpion.html")

# Déconnexion
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("accueil"))

# Lancement du site
if __name__ == "__main__":
    app.run(debug=True)
