
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from background import Background

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)


car_manager = CarManager()

scoreboard = Scoreboard()

background = Background()

player = Player()


screen.listen()
screen.bgcolor("#90BD9C")
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    car_manager.crate_car()
    car_manager.drive()

    if player.ycor() > 260:
        player.goto(0, -270)
        scoreboard.update_level()
        car_manager.faster()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.gameover()
            game_is_on = False


screen.exitonclick()
