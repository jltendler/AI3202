#Jean-Luc Tendler
#CSCI 3202
#Assignment 1
#Due 9/4/15
#Github Username: Jltendler

#1.
import Queue
from time import sleep

class MyQueue:
    def __init__(self):
        self.Queue = Queue.Queue()



    def add(self, item):  #Add into the top slot
		if isinstance(item, int):
			self.Queue.put(item)
		else:
			print "Supplied item is not a number, please retry"

    def remove(self):   
		if self.Queue.empty():
			print "Can't remove from an empty queue!"
			return " "
		else:
			return self.Queue.get()

    
print("*"*80)
print("** Testing Queue **")
q=MyQueue()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.add(5)
q.add(6)
q.add(7)
q.add(8)
q.add(9)
q.add(10)
for i in range(1,10):
	print q.remove()


#2.
class MyStack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
		if self.CheckSize() != 0:
			return self.items.pop()
		else:
			print "Can't pop from an empty stack"

     def CheckSize(self):
         return len(self.items)
print("*"*80)
print("** Testing Stack **")

m=MyStack()
for i in range(1,10):
	m.push(i)
for i in range(1,10):
	print m.pop()



#3.
class MyTree: #http://www.laurentluce.com/posts/binary-search-tree-library-in-python/
	def __init__(self,value):
		self.left = None
		self.right = None
		self.value = value

	def add(self,value,parentValue):
		if self.value == parentValue:  
			if self.left is None:  #ALways fill left first
				self.left = MyTree(value)
			elif self.right is None: #fill right if left full
				self.right = MyTree(value)
			else:
				print "Parent has two nodes, node not added" #both full.
                
                
		else:
			if self.left is not None:
				
				self.left.add(value,parentValue)  #Move to left
			if self.right is not None:
				
				self.right.add(value,parentValue) #move to right try again
			if self.left and self.right is None:
				
				print "Parent not found"  #not found in tree, throw case 4



	def delete(self,value): #recursive delete function.
		if self.left is not None: #Has a left leaf
			if self.left.value == value:  #Case where child of current node is our target
				if self.left.left or self.left.right is not None: #Target has a child. Spare it.
					print "Node not deleted, has children"
				else:
					self.left = None; #No children, no mercy.
			else:
				self.left.delete(value) #Search to the left.
       
		if self.right is not None:
			if self.right.value == value:
				if self.right.left or self.right.right is not None: #Target (on the right) has a child, spare it.
					print "Node not deleted, has children"
				else:
					self.right = None; #no child
			else:
				self.right.delete(value) #Search to right


	def printTree(self): #Print left values, then right values. This results in a kind of mess, but don't need it to be pretty.
		print self.value
		if self.right is not None:
			self.right.printTree()
		if self.left is not None:
			self.left.printTree()
		#if self.left and self.right is None:
			#print "ahoy" #Trying to add a divider - but due to race conditions this doesn't work properly.

print("*"*80)
print("** Testing Tree **")
tree = MyTree(1)
tree.add(2,1)
tree.add(4,1)
tree.add(3,2)
tree.add(5,2)
tree.add(6,3)
tree.add(7,3)
tree.add(8,7)
tree.add(10,7)
tree.add(11,8)
tree.printTree()
print("-------------")
tree.delete(11)
tree.delete(4)
print("Delete 4 and 11.")
tree.printTree()
print("-------------")
#4.
class MyGraph():
	def __init__(self):
		self.dictionary = {}
	def addVertex(self, value):
		if value in self.dictionary:
			print 'Vertex already exists.'
		else:
			self.dictionary[value]=[] #Make a list within the dictionary to store connections to/from this vertex
            
            
	def addEdge(self, value1, value2):
		if value1==value2:
			print "Erm, don't try to add a self-connected vertex here."
		else:
			if value1 in self.dictionary and value2 in self.dictionary: #ensure both vertices exist already

				self.dictionary[value1].append(value2)
				self.dictionary[value2].append(value1)
			else:
				print 'One or more vertices not found.'  #Both verticies don't exist.
            
            
	def findVertex(self, value):
		if value in self.dictionary:
			
			for item in self.dictionary.keys(): #Jess showed you this from her 1300 class.
				if item == value: #found target vertex
					if not self.dictionary[item] :
						print "vertex ", item, "is unconnected =("
					else:
						print 'vertex ', item, 'connects to', self.dictionary[item]
		else: 
			print "Vertex doesn't exist in graph."
print("*"*80)
print("** Testing Graph **")
graph=MyGraph()
graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)
graph.addVertex(6)
graph.addVertex(7)
graph.addVertex(8)
graph.addVertex(9)
graph.addVertex(10)
graph.addVertex(11)
graph.addEdge(1,2)
graph.addEdge(1,4)
graph.addEdge(1,6)
graph.addEdge(1,8)
graph.addEdge(1,10)
graph.addEdge(3,5)
graph.addEdge(3,7)
graph.addEdge(3,9)
graph.addEdge(4,2)
graph.addEdge(4,3)
graph.addEdge(4,5)
graph.addEdge(4,6)
graph.addEdge(4,7)
graph.addEdge(4,8)
graph.addEdge(4,9)
graph.addEdge(6,9)
graph.addEdge(6,10)
graph.addEdge(6,8)
graph.addEdge(10,9)
graph.addEdge(10,8)
#graph.addEdge(1,1)
graph.findVertex(1)
graph.findVertex(2)
graph.findVertex(3)
graph.findVertex(4)
graph.findVertex(5)
graph.findVertex(11)

