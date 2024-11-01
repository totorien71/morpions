# Initialisation de la grille
grille = [[" " for _ in range(3)] for _ in range(3)]

# Fonction pour afficher la grille
def afficher_grille():
    for ligne in grille:
        print("|".join(ligne))
        print("-" * 5)

# Fonction pour vérifier la victoire
def verifier_victoire(symbole):
    # Vérifier les lignes, colonnes et diagonales
    for i in range(3):
        if all(grille[i][j] == symbole for j in range(3)) or all(grille[j][i] == symbole for j in range(3)):
            return True
    if grille[0][0] == grille[1][1] == grille[2][2] == symbole or grille[0][2] == grille[1][1] == grille[2][0] == symbole:
        return True
    return False

# Fonction principale pour jouer au morpion
def jouer():
    joueur = "X"
    for tour in range(9):
        afficher_grille()
        print(f"Tour du joueur {joueur}")
        
        # Choix de la case
        ligne, colonne = map(int, input("Choisissez une ligne et une colonne (0, 1 ou 2) : ").split())
        
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
