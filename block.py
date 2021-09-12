from turtle import Turtle
import random


class Block(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.size = (2, random.randint(5, 9))
        self.shapesize(stretch_wid=self.size[0], stretch_len=self.size[1])
        self.speed(160)