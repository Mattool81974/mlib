from MLib import *

TAILLE=(500, 500)

fenetre=display.set_mode(TAILLE)
app = MFenetre(fenetre, "Mon app", afficherFps=True)
titre = MTexte("Analyseur de texte", (100, 0), (300, 100), app, policeTaille=43)
titreTexte = MTexte("Texte:", (0, 100), (100, 150), app, policeTaille=30, texteAlignement='CC')
texte = MEntreeTexte((100, 100), (300, 150), app, ligneMax=6, policeTaille=18, longueurMax=-1)
titreChar = MTexte("Caractère:", (0, 260), (225, 50), app, policeTaille=30, texteAlignement='CC')
char = MEntreeTexte((225, 260), (50, 50), app, policeTaille=30, texteAlignement="CC", longueurMax=1)
bouton = MBouton("Rechercher", (150, 320), (200, 50), app, actionAuSurvol="policeTaille=38", texteAlignement="CC", policeTaille=34)
resultat = MTexte("Appuyer sur rechercher", (10, 380), (480, 100), app, policeTaille=34, texteAlignement="CC")

while True:
    app.frame()

    if bouton.get_click() and len(char.get_texte()) > 0 and len(texte.get_texte()) > 0:
        nb_occurence = 0
        for i in texte.get_texte():
            if i == char.get_texte():
                nb_occurence += 1
            resultat.set_texte(str(nb_occurence) + " occurences de \"" + char.get_texte() + "\" dans le texte.")
    display.flip()