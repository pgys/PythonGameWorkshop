# Games programmieren mit Python Workshop
# Autor: Peggy Sylopp
# Datum: 8. 5. 2014
# lade ein Hintergrundbild


from turtle import*
shape ("turtle")

setup(width=665, height=700) # wir passen die Größe des Ausgabefensters an
bgpic("maze.gif") # Hintergrundbild soll maze.gif sein

mode("logo") # die Turtle soll nach oben schauen

penup() # die Turtle soll nicht zeichnen

goto(270,-250) # die Turtle soll nach rechts unten gehen (die Mitte des Fensters hat die Koordinaten (0|0) )

fillcolor("green") # die Turtle soll grün sein
