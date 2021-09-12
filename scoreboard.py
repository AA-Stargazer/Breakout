from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, life):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.life = life
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(250, 300)
        self.write(f"scr:{self.score}", align="center", font=("Courier", 80, "normal"))
        self.goto(-250, 300)
        self.write(f"lf:{self.life}", align="center", font=("Courier", 80, "normal"))

    def add_score(self):
        self.score += 1
        self.update_scoreboard()