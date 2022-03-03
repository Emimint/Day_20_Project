from turtle import Turtle

START_LINE_POSITIONS = range(-60, 0, 20)
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):

        self.segments = []

        for turtle_index in range(3):
            name = Turtle(shape="square")
            name.color("white")
            name.penup()
            name.setpos(START_LINE_POSITIONS[turtle_index], 0)
            self.segments.append(name)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)