from turtle import Turtle
import random

COLORS = ["#a8596d", "#df6464", "#ff9f60", "#f9cb57", "#b67d66", "#724d8f", "#8bacc9"]
STARTING_MOVE_DISTANCE = 1.5
MOVE_INCREMENT = 1.5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.all_cars = []

    def crate_car(self):
        random_chance = random.randint(1, 30)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(random.randint(350, 400), random.randint(-230, 230))
            self.all_cars.append(new_car)

    def drive(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def faster(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE +=0.3
        self.drive()