import time
from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open('data.txt', 'r') as data:
            self.greatest_score = int(data.readline())
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.write(f'Score : {self.score}', align='center', font=('Arial', 24, 'normal'))

    def increase(self):
        self.score += 1
        self.write(f'Score : {self.score}', align='center', font=('Arial', 24, 'normal'))

    def lose(self):
        self.speed('fastest')
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('arial', 30, 'normal'))
        time.sleep(2)
        self.clear()
        self.write(f'Greatest Score: {self.greatest_score}', align='center', font=('arial', 30, 'normal'))
