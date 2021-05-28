from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
        self.x = x
        self.shape("square")
        self.speed(0)
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(self.x,0)
    
    # move up
    def up(self):
        self.y = self.ycor()
        self.y = self.y+10
        self.goto(self.x,self.y)

    # move down
    def down(self):
        self.y = self.ycor()
        self.y = self.y-10
        self.goto(self.x,self.y)

    def position(self):
        return [self.xcor(), self.ycor()]