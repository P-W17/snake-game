from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.speed('fastest')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        x_food = random.randint(-280, 280)
        y_food = random.randint(-280, 280)
        self.goto(x_food, y_food)
        self.score += 1

