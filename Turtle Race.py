import turtle
turtle.bgcolor('tan')
import time
#Later on you this will help you make the program stop for a second
import random
red = turtle.Turtle()
#Gives the object/turtle it's name
red.speed(0)
red.penup()
red.goto(-180,140)

number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,]

numberz = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]

list_num = [1,2,3,4,5]

final = [10,9,8,7,6,5,4,3,2,1]
#Lists can be forwards, backwards, or how ever you want

red.write(0)

for number in number_list:
    red.forward(20)
    red.write(number)

red.left(270)
for number in range(21):
    #21 to account for the 0
    red.penup()
    red.goto(-180 + 20 * number,135)
    red.pendown()
    red.forward(200)

red.speed(2)
red.color('red')
red.shape('turtle')
red.left(90)
red.penup()
red.goto(-180,60)

blue = turtle.Turtle()
#That line imports another turtle under a different name; the code can be tweaked to add as many turtles as you want
blue.color('blue')
blue.shape('turtle')
blue.penup()
blue.goto(-180,0)

for number in range(125):
    blue.forward(random.choice(list_num))
    red.forward(random.choice(list_num))
#This loop determines the random speeds of the turtles

winner = 'Blue wins!' if blue.xcor() > red.xcor() else 'Red wins!'
#This line determines the winner(xcor means x-value/how far they went)

referee = turtle.Turtle()
referee.shape('circle')
referee.penup()
referee.write(winner)
referee.left(270)
referee.forward(200)

for number in final:
    referee.shapesize(number * -1)
    time.sleep(0.1)
    #Sleep makes it wait for one second

time.sleep(2)
