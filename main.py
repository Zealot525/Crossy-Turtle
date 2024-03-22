import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move, "w")
screen.onkey(player.back, "s")
screen.onkey(player.left, "a")
screen.onkey(player.right, "d")

cars = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.spawn_rate()
    cars.move_car()
    if player.ycor() >= 280:
        player.go_again()
        scoreboard.increase_score()
        cars.move_increase()
    for car in cars.cars_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            
screen.exitonclick()