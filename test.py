from MLib import *
from time import sleep

TAILLE=(500, 500)

fenetre=display.set_mode(TAILLE)
app = MFenetre(fenetre, "Mon app")
entreeTexte = MEntreeTexte((0, 0), (200, 100), app, policeTaille=24, ligneLongueurMax=170, ligneMax=5, longueurMax=-1)

while True:
    app.frame()

    display.flip()