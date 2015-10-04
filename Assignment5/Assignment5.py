import sys
import math

WorldFile=sys.argv[1]
Eps=float(sys.argv[2])
World=[]
OpenedFile=open(WorldFile)

World=[x.split(" ") for x in OpenedFile.read().split("\n") if x]
print(World)
#World Y/X
#0,0     0,9
     ##
     ##
#7,0     7,9

class Node:
    def __init__(self):
        self.U=0
        self.UPrime=0
        self.Walkable=1
        self.Direction="B"
        self.GammaFactor=0
        self.Occupied=0
    def SetReward(self, reward):
        self.U=reward
    def SetWalkable(self, walkable):
        self.Walkable=walkable
Matrix=[[0 for i in range(10)]for j in range(8)]

for i in range(8):
    for j in range(10):
        Matrix[i][j]=Node()
for i in range(8):
    for j in range(10):
        temp=int(World[i][j])
        if temp==1:
            Matrix[i][j].SetReward(-1)
            Matrix[i][j].Occupied=True
        if temp==2:
            Matrix[i][j].SetWalkable(0)
        if temp==3:
            Matrix[i][j].SetReward(-2)
            Matrix[i][j].Occupied=True
        if temp==4:
            Matrix[i][j].SetReward(1)
            Matrix[i][j].Occupied=True
        if temp==50:
            Matrix[i][j].SetReward(50)
            Matrix[i][j].Occupied=True
        if temp==0:
            Matrix[i][j].SetReward(0)

def InBounds(y,x):
    if(y<0):
        return False
    elif(x<0):
        return False
    elif(y>7):
        return False
    elif (x>9):
        return False
    elif(Matrix[y][x].Walkable==0):
        return False
    else:
        return True
def CalculateUtility(y,x):
    n=0
    e=0
    s=0
    w=0
    n=.8*GetUtility(y-1,x) +.1*GetUtility(y,x-1)+.1*GetUtility(y,x+1)
    e=.8*GetUtility(y,x+1) +.1*GetUtility(y-1,x)+.1*GetUtility(y+1,x)
    s=.8*GetUtility(y+1,x) +.1*GetUtility(y,x-1)+.1*GetUtility(y,x+1)
    w=.8*GetUtility(y,x-1) +.1*GetUtility(y-1,x)+.1*GetUtility(y+1,x)
    if(InBounds(y-1,x)==False):
        n=-1000
    if(InBounds(y,x+1)==False):
        e=-1000
    if(InBounds(y+1,x)==False):
        s=-1000
    if(InBounds(y,x-1)==False):
        w=-1000
    
    
    if max([n,e,s,w])==n:
        Matrix[y][x].Direction="^"
    elif max([n,e,s,w])==e:
        Matrix[y][x].Direction=">"
    elif max([n,e,s,w])==s:
        Matrix[y][x].Direction="V"
    elif max([n,e,s,w])==w:
        Matrix[y][x].Direction="<"
    return max([n,e,s,w])

def GetUtility(y,x):
    #print("Getting Utility of: "+str(y)+","+str(x))
    if(y<0):
        return 0
    elif(x<0):
        return 0
    elif(y>7):
        return 0
    elif (x>9):
        return 0
    elif(Matrix[y][x].Walkable==0):
        return 0
    else:
        return Matrix[y][x].U

def DifferenceChecker():
    print("DIFFER")
    NotGood=0
    for i in range(8):
        for j in range(10):
            difference=abs((Matrix[i][j].U)-Matrix[i][j].UPrime)
            Gamma=.9**Matrix[i][j].GammaFactor
            OneMinus=1-Gamma
            print(i,j)
            if (difference>(Eps*OneMinus)/Gamma):
                    NotGood+=1
            
                
    if NotGood>0:
        return True
    else:
        return False
            



              
times=0
while(DifferenceChecker()):
    times+=1
    print("Iterated Through: "+ str(times)+" times"   )
    
    for i in range(8):
        for j in range(10):
            Matrix[i][j].UPrime=CalculateUtility(i,j)
            Matrix[i][j].GammaFactor+=1

    for i in range(8):
        for j in range(10):
            if(Matrix[i][j].Occupied==False):
                Matrix[i][j].U=(.9**Matrix[i][j].GammaFactor)*(Matrix[i][j].UPrime)
            else:
                Matrix[i][j].UPrime=Matrix[i][j].U
            
DirectionMatrix=[[0 for i in range(10)]for j in range(8)]
for i in range(8):
    for j in range(10):
        if(Matrix[i][j].Walkable==0):
            DirectionMatrix[i][j]="[]"
        else:
            DirectionMatrix[i][j]=Matrix[i][j].Direction
            
UMatrix=[[0 for i in range(10)]for j in range(8)]
for i in range(8):
    for j in range(10):
        if(Matrix[i][j].Walkable==0):
            UMatrix[i][j]="[]"
        else:
            UMatrix[i][j]=Matrix[i][j].U
        
from pandas import *
print DataFrame(DirectionMatrix)
print DataFrame(UMatrix)
