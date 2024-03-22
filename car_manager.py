from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2



class CarManager():
    def __init__(self):
        self.cars_list = []


    def choose_colors(self):
        return random.choice(COLORS)

    def spawn_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid= 1 ,stretch_len= 2)
        new_car.pu()
        new_car.setheading(180)
        new_car.color(self.choose_colors())
        spawn_y_location = random.randrange(-240,240,20)
        new_car.goto(320,spawn_y_location)
        self.cars_list.append(new_car)


    def move_car(self):
        for car in self.cars_list:
            car.fd(STARTING_MOVE_DISTANCE)

    def spawn_rate(self):
        rate = random.randint(0,6)
        if rate == 3:
            self.spawn_car()

    def move_increase(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE  += MOVE_INCREMENT
        