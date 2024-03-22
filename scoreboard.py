FONT = ("Courier", 20, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.pu()
        self.hideturtle()
        self.goto(-280,260)
        self.write(f"level:{self.score}", False, align="left", font=FONT)

    
    def increase_score(self):
        self.clear()
        self.score +=1
        self.write(f"level:{self.score}", False, align="left", font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER.", False, align="left", font=FONT)