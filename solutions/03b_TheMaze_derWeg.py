# Games programmieren mit Python Workshop
# Autor: Peggy Sylopp
# Datum: 8. 5. 2014
# die Turtle läuft den Weg entlang



from turtle import*
shape ("turtle")

setup(width=665, height=700)
bgpic("maze.gif")

mode("logo")
fillcolor("green")
penup()
goto(270,-250)
speed(1) # bewege die Turtle mit der Geschwindigkeit 1
lt(90) # am Start wird die Turtle nach links gedreht


for i in range(2): # hier geht die Turtle den Weg entlang
    forward(540)
    right(90)
    forward(140)
    right(90)
    forward(540)
    left(90)
    forward(140)
    left(90)
