from turtle import Turtle

STEP = 20


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(coordinates)

# Moves the paddle UP direction
    def up(self):
        # self.pong.forward(MOVE_DISTANCE)
        if self.ycor() <= 230:
            new_y = self.ycor() + STEP
            self.goto(self.xcor(), new_y)

# Moves the paddle DOWN direction
    def down(self):
        # self.paddle.backward(MOVE_DISTANCE)
        if self.ycor() >= -230:
            new_y = self.ycor() - STEP
            self.goto(self.xcor(), new_y)



