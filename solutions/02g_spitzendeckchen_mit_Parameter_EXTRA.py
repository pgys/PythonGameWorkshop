# Games programmieren mit Python Workshop
# Autor: Peggy Sylopp
# Datum: 8. 5. 2014
# definiere das Quadrat mit der Seitenlänge als Parameter



from turtle import *

bgcolor("black")

def squad(seitenlaenge): # die Zahl für die seitenlaenge wird erst unten festgelegt
    pencolor("red")
    pensize(1)
    fd(seitenlaenge) # und hier immer eingesetzt
    left(90)
    fd(seitenlaenge)
    left(90)
    fd(seitenlaenge)
    left(90)
    fd(seitenlaenge)
    left(90)

for i in range(30): 
    squad(40) # hier soll die Seitenlänge 40 sein
    left(360/30)

for i in range(40): 
    squad(70) # hier soll die Seitenlänge 70 sein
    left(360/40)

for i in range(60): 
    squad(110) # hier soll die Seitenlänge 110 sein
    left(360/60)
