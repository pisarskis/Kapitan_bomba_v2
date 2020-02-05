import turtle
import math
import random


gm = turtle.Screen()
gm.bgcolor("black")
gm.setup(width=850, height=750, startx=0, starty=0)
speed = 1

border = turtle.Turtle()
border.penup()
border.hideturtle()
border.setposition(-400, -350)
border.color("white")
border.pendown()
border.pensize(1)
for i in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()

# Utworzenie gracza
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()

# Utworzenie planet, ale do przerobienia na obiektówke
max_planets = 7
planets = []
for i in range(max_planets):
    planets.append(turtle.Turtle())
    planets[i].hideturtle()
    planets[i].color("green")
    planets[i].shape("circle")
    planets[i].penup()
    planets[i].setposition(random.randint(-390, 190), random.randint(-340, 240))
    planets[i].showturtle()


def player_turn():

    # Sterowanie gora/dol/lewo/prawo
    # gm.onkey(lambda: player.setheading(90), 'Up')
    # gm.onkey(lambda: player.setheading(180), 'Left')
    # gm.onkey(lambda: player.setheading(0), 'Right')
    # gm.onkey(lambda: player.setheading(270), 'Down')

    # Sterowanie prawo/lewo
    gm.onkey(lambda: player.left(20), 'Left')
    gm.onkey(lambda: player.right(20), 'Right')


def obj_colision(obj1, obj2):
    distance = math.sqrt(math.pow(obj1.xcor() - obj2.xcor(), 2) + math.pow(obj1.ycor() - obj2.ycor(), 2))
    if distance < 20:
        return True
    else:
        return False


gm.listen()
player_turn()

while True:
    player.forward(speed)

    # sprawdzanie granic
    if player.xcor() > 200 or player.xcor() < -400:
        player.right(180)
    elif player.ycor() > 250 or player.ycor() < - 350:
        player.right(180)

    # sprawdzam czy jest kolizja obiektów
    for i in range(max_planets):
        if obj_colision(player, planets[i]):
            speed = 0
