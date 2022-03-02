from turtle import Screen, Turtle
import time

screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


start_line_positions = range(-60, 0, 20)
segments = []
game_is_On = True


def make_a_turtle(position):
    name = Turtle(shape="square")
    name.color("white")
    name.penup()
    name.setpos(position, 0)
    segments.append(name)


for turtle_index in range(3):
    make_a_turtle(start_line_positions[turtle_index])

while game_is_On:
    for piece in segments:
        piece.speed(speed="slowest")
        piece.forward(30)
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
