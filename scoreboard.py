from turtle import Turtle


class Scoreboard(Turtle):

    SCORE = 0

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shapesize(30)
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.show_score()

    def score(self):
        self.clear()
        self.SCORE += 1
        self.show_score()

    def show_score(self):
        self.write(f"Your score is : {self.SCORE}", font=("Arial", 20, "normal"), align="center")

    def write_game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", font=("Arial", 20, "normal"), align="center")