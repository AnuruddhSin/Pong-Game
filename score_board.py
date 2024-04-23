from turtle import Turtle,Screen

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 16, "normal"))
        self.score+=1

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def increse_score(self):
        self.score+=1
        self.clear()
        self.update_score()

