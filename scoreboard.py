from turtle import Turtle


class ScoreBoard (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setPlace()
        self.write(f"Score is : {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))
        self.hideturtle()

    def setPlace(self):
        random_x = 0
        random_y = 260
        self.goto(random_x, random_y)

    def setScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score is : {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))

    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align='center', font=('Arial', 24, 'normal'))

