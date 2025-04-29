from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "vraiment-secret"  # Ne le partage pas si tu mets le site en ligne

# 🔐 Mot de passe que tu donnes à ta famille
PASSWORD = "famille123"

# 🏠 Page d'accueil avec mot de passe
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["motdepasse"] == PASSWORD:
            session["autorise"] = True
            return redirect(url_for("morpion"))
        else:
            return render_template("login.html", erreur="Mot de passe incorrect.")
    return render_template("login.html")

# 🎮 Page du jeu (protégée)
@app.route("/morpion")
def morpion():
    if not session.get("autorise"):
        return redirect(url_for("login"))
    return render_template("morpion.html")

# 🔁 Permet à ta famille de se déconnecter
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# 🚀 Lancer l'application
if __name__ == "__main__":
    app.run(debug=True)
