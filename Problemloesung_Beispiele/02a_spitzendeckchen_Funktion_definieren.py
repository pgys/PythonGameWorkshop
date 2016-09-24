# Games programmieren mit Python Workshop
# Autor: Peggy Sylopp
# Datum: 8. 5. 2014
# definiere das Quadrat als Funktion, rufe die Funktion auf


from turtle import*
shape ("turtle")

bgcolor("black") 
pencolor("red")


def quadrat():   # "quadrat()" soll die neue Abkürzung für die eingerückten Anweisungen darunter sein
    fd(100) 
    lt(90)
    fd(100) 
    lt(90)
    fd(100) 
    lt(90)
    fd(100) 
    lt(90)


quadrat() # zeichne ein Quadrat, wie es oben definiert ist
