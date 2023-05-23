from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.shapesize(1,1)
        self.up()
        self.x_move = 10
        self.y_move = 10
        self.level = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def bounce(self):
        self.y_move *= -1

    def reflect(self):
        self.x_move *= -1
        self.level *= 0.9

    def reset_position(self):
        self.goto((0,0))
        self.level = 0.1
        self.reflect()




