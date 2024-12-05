from turtle import Turtle,Screen
import random

snake=Turtle()
screen=Screen()
screen.setup(600,600)
screen.title("Snake Game")
screen.bgcolor("black")
snake.speed(0.05)
screen.tracer(0)


x_positions = [-40, -20, 0]
all_snakes = []
#Create 6 turtles
for snake_index in range(0,3):
    new_snake= Turtle(shape="square")
    new_snake.penup()
    new_snake.color('white')
    new_snake.goto(y=0 , x=x_positions[snake_index])
    all_snakes.append(new_snake)

screen.update()

while True:
    for i in range(0,3):
        new_snake.forward(50)

screen.update()

for i in range(0,3):
    snake=all_snakes[i]

#new_snake()
def move():
    snake.forward(50)
def back():
    snake.backward(50)
def left():
    snake.left(90)
def right():
    snake.right(90)
def clear():
    snake.clear()
    snake.penup()
    snake.home()
    snake.pendown()

screen.listen()
screen.onkey(key='w',fun=move)
screen.onkey(key='s',fun=back)
screen.onkey(key='a',fun=left)
screen.onkey(key='d',fun=right)





screen.exitonclick()
screen.onkey()