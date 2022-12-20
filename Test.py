from MLib import *

fenetre=display.set_mode((500, 500))
app=MFenetre(fenetre, "Mon app")
widgetParent=MBordure((10, 10), (200, 200), app, bordureLargeur=2, borduresLargeurs=[10, None, 30, None])
widget=MEntreeTexte((10, 10), (100, 100), widgetParent, policeTaille=18, arrierePlanCouleur=(255, 0, 0, 1))

while True:
    app.frame()

    display.flip()