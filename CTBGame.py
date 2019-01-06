import random
import numpy
class Game:
    def __init__(self,a1,a2,a3,a4,a5,a6,a7,a8,a9):
        self.nums = [1,a1,a2,a3,a4,a5,a6,a7,a8,a9]
        #a0 location is always available
        self.points = 0
        self.pointsvect = 0
        self.dice = 0
        self.dicevect = 0
        self.moves = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],
                        [1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],
                        [2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],
                        [3,4],[3,5],[3,6],[3,7],[3,8],[3,9],
                        [4,5],[4,6],[4,7],[4,8],
                        [5,6],[5,7]]
        self.availmoves = []
        
    def roll(self):
        self.dice = random.randint(1,6) + random.randint(1,6)
        self.dicevect = (self.dice) / 12
    def getmoves(self):
        self.availmoves=[]
        for i in range(0,len(self.moves)):
            a = self.moves[i][0]
            b = self.moves[i][1]
            if ((a+b==self.dice) & (self.nums[a]==1) & (self.nums[b]==1)):
                self.availmoves.append(i)
    def startturn(self):
        self.roll()
        self.getmoves()
    def startturn_cheat(self,dice):
        if(dice>12):
            dice=12
        if(dice<2):
            dice=2
        self.availmoves=[]
        self.dice=dice
        self.getmoves()
    def makemove(self,index):
        chosenmove = self.moves[index]
        for tile in chosenmove:
            self.nums[tile]=0
        self.nums[0]=1
    def gameover(self):
        if (len(self.availmoves)==0):
            return 1
        else:
            return 0
    def iwon(self):
        if (self.nums==[1,0,0,0,0,0,0,0,0,0]):
            return 1
        else:
            return 0
    def getscore(self):
        total = 0
        maxnum = 10
        for number in self.nums[1:]:
            total = total+1
        if total==0:
            return 1
        else:
            return (0.7*(1-(total/maxnum)))
    def showdice(self):
        return self.dice
    def showmoves(self):
        return self.availmoves
    def showenv_val(self):
        return self.nums+[self.dice]
    def showenv_vect(self):
        return numpy.asarray(self.nums+[self.dicevect])