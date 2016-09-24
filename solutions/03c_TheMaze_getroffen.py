# Games programmieren mit Python Workshop
# Autor: Peggy Sylopp
# Datum: 8. 5. 2014
# Treffer anzeigen - die Spiele-"Engine"

from turtle import*
shape ("turtle")

setup(width=665, height=700)
bgpic("maze.gif")

mode("logo")
fillcolor("green")
penup()
goto(270,-250)
speed(1)
left(90)

def getroffen(x,y): # wenn die Turtle getroffen wird, soll sie "erröten"
    fillcolor("red")

onclick(getroffen) # klickst du auf die Turtle, ist sie getroffen

for i in range(2):
    forward(540)
    right(90)
    forward(140)
    right(90)
    forward(540)
    left(90)
    forward(140)
    left(90)


