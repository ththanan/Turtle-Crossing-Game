from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("#33514A")
        self.current_level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level: {self.current_level}", align="center", font=FONT)
        self.current_level += 1

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
