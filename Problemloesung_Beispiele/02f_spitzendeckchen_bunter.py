# Games programmieren mit Python Workshop
# Autor: Peggy Sylopp
# Datum: 8. 5. 2014
# das Mandala etwas komplexer


from turtle import*
shape ("turtle")

bgcolor("red") # Hintergrundfarbe rot

speed(10)

def kleinesquadrat():   
    pencolor("yellow") # Stiftfarbe gelb
    fd(50) 
    lt(90)
    fd(50) 
    lt(90)
    fd(50) 
    lt(90)
    fd(50) 
    lt(90)

def groesseresquadrat():  
    pencolor("green") # Stiftfarbe grün
    fd(100) 
    lt(90)
    fd(100) 
    lt(90)
    fd(100) 
    lt(90)
    fd(100) 
    lt(90)

for i in range(30): 
    kleinesquadrat() 
    lt(360/30) 

for i in range(60): 
    groesseresquadrat()
    lt(360/60)


