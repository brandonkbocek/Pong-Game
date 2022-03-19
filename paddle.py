from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = 0
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(self.x_pos, self.y_pos)


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)