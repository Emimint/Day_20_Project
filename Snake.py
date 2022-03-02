from turtle import Screen, Turtle

start_line_positions = range(-60, 0, 20)
segments = []

def __init__(self):
    for turtle_index in range(3):
        name = Turtle(shape="square")
        name.color("white")
        name.penup()
        name.setpos(self.start_line_positions[turtle_index], 0)
        self.segments.append(name)

def add_segment(position):
    name = Turtle(shape="square")
    name.color("white")
    segments.append(name)

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)



def move():
    screen.listen()
    screen.onkey(move_forwards, "Up")
    screen.onkey(move_backwards, "Down")
    screen.onkey(turn_left, "Left")
    screen.onkey(turn_right, "Right")

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)