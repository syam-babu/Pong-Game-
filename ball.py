from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.dx = .3
        self.dy = .3

    def movement(self):
        x=self.xcor() + self.dx
        y=self.ycor() + self.dy
        self.goto(x,y)
        
    
    def wall_Collision(self):
        if (self.ycor()>290) or (self.ycor()<-290):
            self.dy *=(-1)
    

    def reset(self): 
        if (self.xcor()>400) or (self.xcor()<-400):
            bool = self.xcor()<0
            self.dx*=-1
            self.goto(0,0)
            return [True,bool]
        else:
            return [False]
            
    def pad_Collision(self,pad_r,pad_l):
        
        if self.distance(pad_r) < 50 and self.xcor() > 340 or self.distance(pad_l) < 50 and self.xcor() < -340:
            self.dx*=(-1)

            
