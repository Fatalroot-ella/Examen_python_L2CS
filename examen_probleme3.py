#PROBLEME 3 DESSIN GRAPHIQUE AVEC TURTLE

import turtle
import random
def demander_utilisateur_entier_0_9():
    while True:
        try:
            n = int(input("Veuillez entrer un entier entre 0 et 9  : "))
            if 0 <= n <= 9:
                return n
            else:
                print("Erreur : L'entier doit être entre 0 et 9.")
        except ValueError:
            print("Erreur : Veuillez entrer un entier valide.")

def dessiner_forme(t, forme):
    taille = random.randint(100, 400)
    if forme == 'carré' or forme == 'carre':
        for _ in range(4):
            t.forward(taille)
            t.right(90)

    elif forme == 'triangle':
        for _ in range(3):
            t.forward(taille)
            t.left(120)

    else:
        forme == 'circle' or forme == "cercle"
        if forme == 'cercle':
            t.circle(taille/2)
