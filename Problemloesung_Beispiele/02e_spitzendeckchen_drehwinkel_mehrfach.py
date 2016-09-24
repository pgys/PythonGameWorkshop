# Games programmieren mit Python Workshop
# Autor: Peggy Sylopp
# Datum: 8. 5. 2014
# den drehwinkel für das Quadrat bestimmen


from turtle import*
shape ("turtle")

bgcolor("black")

pencolor("red")

speed(10) 

def kleinesquadrat():   # "kleinesquadrat()" soll Seitenlänge 50 haben
    fd(50) 
    lt(90)
    fd(50) 
    lt(90)
    fd(50) 
    lt(90)
    fd(50) 
    lt(90)
    
for i in range(30): # führe die eingerückten Anweisungen 30mal aus
    kleinesquadrat() # Quadrat zeichnen (30mal)
    lt(360/30) # 360/30 Grad nach links drehen

def groesseresquadrat():   # "groesseresquadrat()" soll Seitenlänge 100 haben
    fd(100) 
    lt(90)
    fd(100) 
    lt(90)
    fd(100) 
    lt(90)
    fd(100) 
    lt(90)

for i in range(60): # führe die eingerückten Anweisungen 60mal aus
    groesseresquadrat() # Quadrat zeichnen (60mal)
    lt(360/60) # 360/60 Grad nach links drehen


