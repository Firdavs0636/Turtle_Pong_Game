from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')

        # Used for previous version of bouncing a ball
        # self.new_x = 0
        # self.new_y = 0

        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.08

    # def ball_move(self, x_cor, y_cor):

# Moves the ball
    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

# Reverses the Y coordination value
    def bounce_y(self):

        # Previous version
        # self.goto(x=self.new_x, y=self.new_y)
        # self.new_x += BALL_STEP
        # self.new_y -= BALL_STEP

        self.y_move *= -1

# Reverses the X coordination value
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

# Resets the Ball to its initial position and reverses its direction
    def reset_ball(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()

    # def ball_accelerate(self):
    #     # self.x_move += 1
    #     pass



