from MLib import *

fenetre=display.set_mode((500, 500))
app=MFenetre(fenetre, "Mon app")
widgetParent=MBordure((10, 10), (200, 200), app)
widget=MBordure((10, 10), (100, 100), widgetParent, arrierePlanCouleur=(255, 0, 0, 1))

while True:
    app.frame()

    print(widget.get_position(), widget.get_globalPosition())

    widget.set_position((50, 50))

    app.frame()

    print(widget.get_position(), widget.get_globalPosition())

    exit()

    display.flip()