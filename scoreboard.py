from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 12, 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.collision_counter = 0
        self.color("white")
        self.penup()
        self.shape("blank")
        self.goto(-20, 270)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score = {self.collision_counter}", False, align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", False, align=ALIGNMENT, font=FONT)