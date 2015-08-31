#Jean-Luc Tendler
#CSCI 3202
#Assignment 1
#Due 9/4/15

#1.
import Queue

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

    
'''
q=MyQueue()
q.add(1)
q.add(3)
q.add(4)
q.add(5)
q.add("potato")
print q.remove()
print  q.remove()
print q.remove()
print q.remove()
print q.remove()
'''
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
'''
m=MyStack()
m.push(14)
m.push("woof")
m.push("bark")
print m.pop()
print m.pop()
print m.pop()
print m.pop()

'''
#3.
class MyNode(object):
	def __init__(self, value, parent):
		
		if not isinstance(value, int):
			print "Value is not an integer. Please use an integer. You probably just broke everything."
		else:	
			self.key = value
			self.left = None
			self.right = None
			self.parent = parent

class MyTree(object):
	
	#http://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree-in-python some guidance
	def __init__(self):
		self.root = None


