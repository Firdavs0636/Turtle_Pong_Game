from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')


class Board(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.color('#4aefe4')
        self.penup()
        self.ht()
        self.goto(x=x_cor, y=275)
        self.scores = 0
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f'Score: {self.scores}', align=ALIGNMENT, font=FONT)
        self.scores += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', move=True, align=ALIGNMENT, font=FONT)

