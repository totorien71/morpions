import tkinter as tk
from tkinter import messagebox
# Initialisation de la grille
grille = [[" " for _ in range(3)] for _ in range(3)]

# Fonction pour afficher la grille
def afficher_grille():
    for ligne in grille:
        print("|".join(ligne))
        print("-" * 5)

# Fonction pour vérifier la victoire
# snake_case
# PascalCase
# camelCase
def verifier_victoire(symbole):
    # Vérifier les lignes, colonnes et diagonales
    for i in range(3):
        if all(grille[i][j] == symbole for j in range(3)) or all(grille[j][i] == symbole for j in range(3)):
            return True
    if grille[0][0] == grille[1][1] == grille[2][2] == symbole or grille[0][2] == grille[1][1] == grille[2][0] == symbole:
        return True
    return False

def input_is_valid(user_input):
    res = False
    try:
        ligne, colonne = map(int, user_input.split())
        res = True
    except ValueError:
        print("Format invalide. Veuillez entrer deux chiffres séparés par un espace, une virgule ou sans séparateur.")
    return res

# Fonction principale pour jouer au morpion
def jouer():
    joueur = "X"
    for tour in range(9):
        afficher_grille()
        print(f"Tour du joueur {joueur}")
        
        saisie = input("joue")
        while not input_is_valid(saisie) : saisie = input("joue")

        # Choix de la case
        ligne, colonne = map(int, saisie.split())
        
        # Vérification si la case est libre
        if grille[ligne][colonne] == " ":
            grille[ligne][colonne] = joueur
            # Vérification de victoire
            if verifier_victoire(joueur):
                afficher_grille()
                print(f"Le joueur {joueur} a gagné !")
                return
            # Changer de joueur
            joueur = "O" if joueur == "X" else "X"
        else:
            print("Cette case est déjà occupée. Choisissez une autre case.")
    
    afficher_grille()
    print("Match nul !")

# Lancer le jeu
jouer()
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
