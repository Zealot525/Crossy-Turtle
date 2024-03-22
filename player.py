STARTING_POSITION_X = 0
STARTING_POSITION_Y = -280
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.color("black")
        self.pu()
        self.setheading(90)
        self.goto(STARTING_POSITION_X,STARTING_POSITION_Y)

    def position_checker(self):
        if self.ycor() < STARTING_POSITION_Y or self.xcor() > 280 or self.xcor <-280:
            new_x = self.xcor() - 20
            new_y = self.ycor() - 20
            self.goto(new_x, new_y)

    def move(self):
        self.setheading(90)
        self.fd(MOVE_DISTANCE)

    def back(self):
        self.setheading(270)
        self.fd(MOVE_DISTANCE)

    def left(self):
        self.setheading(180)
        self.fd(MOVE_DISTANCE)

    def right(self):
        self.setheading(0)
        self.fd(MOVE_DISTANCE)

    def go_again(self):
        if self.ycor() >= FINISH_LINE_Y:
            current_X = self.xcor()
            self.goto(current_X,STARTING_POSITION_Y)