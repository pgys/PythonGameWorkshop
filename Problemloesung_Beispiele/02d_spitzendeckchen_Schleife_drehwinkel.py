# Games programmieren mit Python Workshop
# Autor: Peggy Sylopp
# Datum: 8. 5. 2014
# definiere eine Schleife



from turtle import*
shape ("turtle")

bgcolor("black")

pencolor("red")

speed(10) # die Turtle soll sich beeilen ;-)

def quadrat():  
    fd(100)    # das Quadrat hat eine Seitenlänge von 100 Pixel
    lt(90)
    fd(100) 
    lt(90)
    fd(100) 
    lt(90)
    fd(100) 
    lt(90)

for i in range(30): # führe die eingerückten Anweisungen darunter 30 mal aus
    quadrat() # Quadrat zeichnen (30 mal)
    lt(360/30) # 360/30 Grad nach links drehen




