from turtle import Turtle


class Scoreboard(Turtle):

    SCORE = 0

    def __init__(self):
        super().__init__()
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
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
        self.write(f"Your score is : {self.SCORE}.Your high score is {self.high_score}", font=("Arial", 20, "normal"), align="center")

    def write_game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", font=("Arial", 20, "normal"), align="center")