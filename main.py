from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from board import Board

RIGHT_PADDLE_COORDINATE = (350, 0)
LEFT_PADDLE_COORDINATE = (-350, 0)
RIGHT_SCOREBOARD_X = 80
LEFT_SCOREBOARD_X = -80


ball = Ball()

l_board = Board(LEFT_SCOREBOARD_X)
r_board = Board(RIGHT_SCOREBOARD_X)


screen = Screen()
screen.title('Pong Game')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0, 0.1)

paddle_r = Paddle(RIGHT_PADDLE_COORDINATE)
paddle_l = Paddle(LEFT_PADDLE_COORDINATE)

screen.listen()
screen.onkey(paddle_r.up, 'Up')
screen.onkey(paddle_r.down, 'Down')
screen.onkey(paddle_l.up, 'w')
screen.onkey(paddle_l.down, 's')

y_cor = 2
x_cor = 2

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(ball.move_speed)

    # Previous version of ball bouncing and collision with wall
    # ball.ball_move(x_cor, y_cor)
    #
    # if ball.ycor() > 280 and ball.xcor() > 0:
    #     y_cor = -1
    #
    # elif ball.ycor() < -280 and ball.xcor() > 0:
    #     y_cor = +2
    #
    # elif ball.ycor() > 280 and ball.xcor() < -0:
    #     y_cor = -2
    #     x_cor = -2
    #
    # elif ball.ycor() < -280 and ball.xcor() < -0:
    #     y_cor = +2
    #     x_cor = -2

    ball.ball_move()

# Detecting COLLISION with Upper and Bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# Detecting COLLISION with right paddle
    elif ball.distance(paddle_r) < 50 and ball.xcor() > 340:
        ball.bounce_x()

# Detecting COLLISION with left paddle
    elif ball.distance(paddle_l) < 50 and ball.xcor() < -340:
        ball.bounce_x()

# Detecting COLLISION with Right side of the wall
    elif ball.xcor() == 380:
        ball.reset_ball()
        l_board.update()

# Detecting COLLISION with Left side of the wall
    elif ball.xcor() == -380:
        ball.reset_ball()
        r_board.update()

screen.exitonclick()
