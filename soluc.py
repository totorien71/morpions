import tkinter as tk
from tkinter import messagebox

# Initialisation de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Jeu du Morpion")

# Variables pour suivre le tour et l'état du jeu
joueur = "X"
plateau = [["" for _ in range(3)] for _ in range(3)]

# Fonction pour vérifier la victoire
def verifier_victoire():
    # Vérifie les lignes, les colonnes et les diagonales
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != "":
            return True
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != "":
            return True
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != "" or plateau[0][2] == plateau[1][1] == plateau[2][0] != "":
        return True
    return False

# Fonction pour gérer le clic sur une case
def cliquer(x, y):
    global joueur
    if plateau[x][y] == "" and not verifier_victoire():
        # Met à jour le plateau et le bouton
        plateau[x][y] = joueur
        boutons[x][y].config(text=joueur, state="disabled")
        
        # Vérifie si le joueur actuel a gagné
        if verifier_victoire():
            messagebox.showinfo("Victoire", f"Le joueur {joueur} a gagné !")
            fenetre.quit()  # Ferme la fenêtre à la fin
        elif all(plateau[i][j] != "" for i in range(3) for j in range(3)):
            # Si toutes les cases sont remplies sans gagnant
            messagebox.showinfo("Match nul", "Match nul !")
            fenetre.quit()
        else:
            # Change de joueur
            joueur = "O" if joueur == "X" else "X"

# Création des boutons pour le plateau
boutons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        boutons[i][j] = tk.Button(fenetre, text="", font=("Arial", 20), width=5, height=2,
                                  command=lambda x=i, y=j: cliquer(x, y))
        boutons[i][j].grid(row=i, column=j)

# Lancer la boucle principale de l'interface
fenetre.mainloop()
