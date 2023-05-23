from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.create_paddle()
        self.goto(position)

    def create_paddle(self):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
