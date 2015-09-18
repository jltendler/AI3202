#Jean-Luc Tendler
#CSCI 3202
#Assignment 3
#Due 9/18/15
#Github Username: Jltendler




#some stuff referred to: http://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/
#http://scriptogr.am/jdp/post/pathfinding-with-python-graphs-and-a-star
#http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html

import sys
import math
import Queue



class Search():
    def __init__(self, PassedWorld, h):

        self.World = PassedWorld
        self.rows = len(PassedWorld)
        self.columns = len(PassedWorld[0])
        self.start = ((self.rows - 1), 0)  #We start at bottom left
        self.end = (0, self.columns - 1) #And end at top right.   This is hardcoded grossness, but works here.

        self.Search(h)
        
        





    def neighbors(self, currentPosition): #returns what you can get to from where you are.
        def Inbounds(xy):
            x=xy[0]
            y=xy[1]
            
            a=x>-1 #Checking it's in world
            b=x<self.rows  #Checking in world
            c=y>-1 #not below world
            d=y<self.columns #Not above world
            return a and b and c and d
        x=currentPosition[0]
        y=currentPosition[1]        
        surroundingNodes = [(x-1, y), (x-1, y+1), (x,y+1), (x+1,y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1)]
        canTravelTo=[]
        for xy in surroundingNodes:
			if (Inbounds(xy) and (self.isWall(xy)==False)):
				canTravelTo.append(xy)
        return canTravelTo #tested working - done for today
        
        

    def isMountain(self, myTuple):
        if int(self.World[myTuple[0]] [myTuple[1]]) == 1:
            return True
        else:
            return False
    def isWall(self, myTuple):
        if int(self.World[myTuple[0]] [myTuple[1]]) == 2:
            return True
        else:
            return False

    def manhattan(self, first, second): #http://heuristicswiki.wikispaces.com/Manhattan+Distance
        return((abs(first[0] - second[0]) + abs(first[1] - second[1])*10))

    def euclidian(self, first, second): #https://lyfat.wordpress.com/2012/05/22/euclidean-vs-chebyshev-vs-manhattan-distance/
        return 10 * math.sqrt(((first[1] - second[1])*(first[1]-second[1])) + ((first[0] - second[0])*(first[0]-second[0])))

    def cost(self, currentNode, destination):
        if (int(self.manhattan(currentNode, destination)) == 10):

            cost = 10 #NESW move
        else:
            #print(int(self.manhattan(currentNode, next)))
            cost = 14 #Any time it's a diagonal move.
        if (self.isMountain(destination)):
            return cost+10
        return cost

    def Search(self, h):

        previousNode = {self.start: None}
        TheQ = Queue.PriorityQueue()
        BackwardsQ=[]
        TheQ.put((0, self.start)) 
        locationsEvaluated = 0
        explored=[]
        costSoFar = {self.start: 0}
        
        
        #need an output function for the nodes travelled to.
        def printer(currentNode):
            while (not currentNode == None):
                currentNode = previousNode[currentNode]
                BackwardsQ.insert(0,currentNode)
            BackwardsQ.pop(0)
            BackwardsQ.append(self.end)
            print BackwardsQ
            
            
        while (not TheQ.empty()):
            currentNode = TheQ.get()[1] #Returns a tuple of (value, (coordinates)), so we just wanna grab the first part. (https://docs.python.org/2/library/queue.html)
            if (currentNode == self.end): #Our journey is at an end.
                print ("A Path costing: " + str(costSoFar[self.end]+10) + " Has been found.")  #Adding 10 because it doesn't consider the last move.
                print ("It took us " + str(len(explored)) + " node evaluations to get us here.")
                printer(self.end)
                TheQ.get()[1] #Empty the Q to escape while loop.

            for potentialNode in self.neighbors(currentNode):
                newCost = costSoFar[currentNode] + self.cost(currentNode, potentialNode)
                if potentialNode not in costSoFar or newCost < costSoFar[potentialNode]: #1. Haven't been there, 2. It's cheaper this way
                    costSoFar[potentialNode] = newCost
                    if (h == 1):
                        f = newCost + self.manhattan(potentialNode, self.end)
                    elif(h==2):
                        f = newCost + self.euclidian(potentialNode, self.end)
                    else:
                        print("Trying to do stuff without a valid heuristic is hard. Please see how to use this program.")
                    TheQ.put((f, potentialNode))
                    previousNode[potentialNode] = currentNode
                if(potentialNode not in explored): #Adding nodes to our explored list so we have a count.
                    explored.append(potentialNode)
                if(currentNode not in explored):
                    explored.append(currentNode)   #Adding nodes to our explored list so we have a count.
                
###
###
###
#####Handling all the argv stuff, and matrixizing the data.
WorldFile=sys.argv[1]
h=sys.argv[2]
h=int(h)
World=[]

OpenedFile=open(WorldFile)

World=[x.split(" ") for x in OpenedFile.read().split("\n") if x]
#print World  #now we have a nice matrix.

if (h is not 1 and h is not 2):
	print("Please check the readme, your input is invalid.")
print("Using Heuristic: " +str(h))

Search(World,h)

