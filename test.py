from MLib import *

TAILLE=(500, 500)

fenetre=display.set_mode(TAILLE)
app = MFenetre(fenetre, "Mon app")
entree = MEntreeTexte((0, 0), (200, 200), app, policeTaille=38, texteAlignement="GH")

while True:
    app.frame()
    display.flip()