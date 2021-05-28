from turtle import Turtle  

class ScoreBoard(Turtle):
    player_A=0
    player_B=0
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.color('white')
        self.shape('square')
        self.goto(0,250)
        self.hideturtle()
        self.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "normal"))
        

    def update(self,bool):
        # if bool = True, point for player B 
        if bool:
            ScoreBoard.player_B+=1
            self.rewrite(ScoreBoard.player_A,ScoreBoard.player_B)
        else:
            ScoreBoard.player_A+=1
            self.rewrite(ScoreBoard.player_A,ScoreBoard.player_B)

    def rewrite(self,player_A,player_B):
        self.clear()
        self.write("Player A: {}  Player B: {}".format(player_A,player_B), align="center", font=("Courier", 20, "normal"))
        