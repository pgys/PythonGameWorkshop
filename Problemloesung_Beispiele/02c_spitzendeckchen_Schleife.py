# Games programmieren mit Python Workshop
# Autor: Peggy Sylopp
# Datum: 8. 5. 2014
# definiere ein Quadrat als Funktion, Schleife programmieren


from turtle import*
shape ("turtle")

bgcolor("black") 
pencolor("red")


def quadrat():   
    fd(100) 
    lt(90)
    fd(100) 
    lt(90)
    fd(100) 
    lt(90)
    fd(100) 
    lt(90)

# die Abkürzung für die Drehung:

for i in range(30): # führe die eingerückten Anweisungen darunter 30mal aus
    quadrat() # Quadrat zeichnen
    lt(30) # 30 Grad nach links drehen
