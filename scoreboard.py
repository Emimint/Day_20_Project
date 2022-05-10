from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 12, 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("score_data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.shape("blank")
        self.goto(-20, 270)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score = {self.score} High score: {self.high_score}", False, align= ALIGNMENT, font= FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_data.txt","w") as file:
                file.write(str(self.high_score))
        self.refresh()
        self.score = 0
        self.refresh()