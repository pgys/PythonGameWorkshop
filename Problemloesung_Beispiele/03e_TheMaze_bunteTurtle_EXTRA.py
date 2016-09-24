# Games programmieren mit Python Workshop
# Autor: Peggy Sylopp
# Datum: 8. 5. 2014
# die Turtle ändert beim Anklicken jedes Mal erneut die Farbe



from turtle import*
from random import*

shape ("turtle")

setup(width=665, height=700)
bgpic("maze.gif")

mode("logo")
fillcolor("green")
penup()
goto(270,-250)
speed(1)
left(90)
colors=["white", "red3", "yellow", "blue4", "green", "yellow3", "orange", "red", "blue", "green4"]
farbe =0

treffer = 0
turtle = Turtle()
turtle.hideturtle()
turtle.pu()
turtle.goto(-135,-325)
turtle.pencolor("white")
turtle.write("Triff die Turtle!", font=("Arial", 14, "bold"))


def getroffen(x,y):
    global farbe
    farbe += 1
    fillcolor(colors[farbe%10])
    global treffer
    turtle.clear()
    treffer +=1
    turtle.write("Du hast " + str(treffer) + " Mal getroffen!",  font=("Arial", 14, "bold"))

onclick(getroffen)

for i in range(2):
    forward(540)
    right(90)
    forward(140)
    right(90)
    forward(540)
    left(90)
    forward(140)
    left(90)

