from turtle import Screen, Turtle
import time
import Snake

screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()

game_is_On = True

while game_is_On:
    screen.update()
    time.sleep(0.5)

screen.exitonclick()
