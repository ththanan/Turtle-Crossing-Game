from turtle import Turtle

class Background(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("#d9d9cc")
        self.shapesize(stretch_wid=25, stretch_len=40)