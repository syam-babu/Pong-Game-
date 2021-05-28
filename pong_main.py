import turtle  
from ball import Ball
from paddle import Paddle 
from scoreboard import ScoreBoard 
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("PONG!!!!!")
wn.setup(width=800, height=600)
wn.tracer(0)

ball = Ball()
paddle_left = Paddle(x=-350)
paddle_right = Paddle(x=350)
score = ScoreBoard()


wn.listen()
wn.onkeypress(paddle_left.up, "w")
wn.onkeypress(paddle_left.down, "s")
wn.onkeypress(paddle_right.up, "Up")
wn.onkeypress(paddle_right.down, "Down")


while True:
    wn.update()
    ball.movement()
    ball.wall_Collision()
    ball.pad_Collision(paddle_right,paddle_left)
    r = ball.reset() #returns a tuple of 2 boolean values,first to check if game had been reset, second to signify which side got point
    print(type(r))
    if r[0]:
        score.update(r[1])
        wn.update()
        time.sleep(1)
