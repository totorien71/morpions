from flask import Flask

app = Flask (__name__)

@app.route('/')
def accueil():
    return "bienvenue sur mon site web en python!"

if __name__ == '__main__':
    app.run(debug=True)