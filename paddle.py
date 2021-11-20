from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        # create paddle
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x_cor, y=y_cor)

    def right_go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def right_go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def left_go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def left_go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)