# Games programmieren mit Python Workshop
# Autor: Peggy Sylopp
# Datum: 8. 5. 2014
# das Mandala erstellen, wie drehe ich das Quadrat?


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

# Jetzt kommt die Drehung ...

quadrat() # zeichne ein Quadrat
lt(80) # drehe die Turtle etwas
quadrat() # nochmal Quadrat zeichnen
lt(80) # nochmal drehen ...
quadrat() 
lt(80)
quadrat() 
lt(80)


