import getopt,sys


class Node:
	def __init__(self,name):
		self.title = name
		self.probability = 0
	def GetTitle(self):
		return self.title
	def GetProbability(self):
		return self.probability
	def GetInverseProbability(self):
		return 1-self.probability
	def SetProbability(self,value):
		self.probability=value

def Network(pV,sV): #Network is made here.

	#Build Nodes
	p=Node("pollution")
	s= Node("smoker")
	#Setting inititally given values.
	p.SetProbability(pV)
	s.SetProbability(sV)
	c= Node("cancer")
	d= Node("dyspnoea")
	x= Node("xray")
#x node
#.9,.2
	HasCancer=   c.GetProbability()*.9
	NoCancer=c.GetInverseProbability()  * .2
	x.SetProbability(HasCancer+NoCancer)

#c node
#   ~ps,~p~s,ps,p~s
#.05,.02,.03,.001
	pNotpS =      p.GetInverseProbability() *s.GetProbability()*.05
	pNotpNotS =   p.GetInverseProbability()*s.GetInverseProbability()*.02
	pPS =         p.GetProbability()*s.GetProbability()*.03
	pPNotS=       p.GetProbability()*s.GetInverseProbability()*.001
	c.SetProbability(pNotpS+pNotpNotS+pPS+pPNotS)  #Total probability is that of it's 4 possibilities.
#dnode
#c,~c
#.65,.3
	HasCancer=  c.GetProbability() *.65
	NoCancer=c.GetInverseProbability() *.3
	d.SetProbability(HasCancer+NoCancer)


	network = {}
	network["p"] = p
	network["s"] = s
	network["c"] = c
	network["d"] = d
	network["x"] = x
	
	#This creates a set of these 5 objects which we can then refer to as network["Z"].whatever
	return network
	
	
def marginal(arg,network): #Returns marginal probability of arg
	temp = 999  #If you ever see 999 something is really wrong.
	cancerval=network["c"].GetProbability()
	
	
	if (arg == 'p'):
		temp = network[arg].GetProbability() #Just check pollution probability
	elif (arg == 's'):
		temp= network[arg].GetProbability()#Just check smoker probability
	elif (arg == 'c' ):
		temp= network[arg].GetProbability() #Just check cancer probability.
	elif (arg == 'd' ):
		temp= (cancerval * network[arg].GetProbability()) + ( (1-cancerval) * network[arg].GetProbability())
		#This is the probability of cancer, times the probability of D. + The probability of not cancer and D. Both of these together is our odds of D
	elif (arg == 'x' ):
		temp= (cancerval * network[arg].GetProbability()) + ( (1-cancerval) * network[arg].GetProbability())
	return temp
def marginalInverse(arg,network): #Just returns 1-marginal.
	return(1-marginal(arg,network))

def conditional(first,second,network): #doesn't work
	network[second].SetProbability(1)
	if(first=="c" and second=="p"):#No idea.
		print("")
		#I would have to remake the network entirely using new values. Not sure how to implement this.
	return "Unimplemented"
		

def setPrior(variable,value,network): #Changes the probability of variable to value in network.
	network[variable].SetProbability(value)
	print "P of " +network[variable].GetTitle() + " has been set to " + str(network[variable].GetProbability())

def main():
	p = .9 #Given probability of pollution.
	s = .3 #Given probability of smoker.
	network= Network(p,s)

	try:
		opts, args = getopt.getopt(sys.argv[1:], "m:g:j:p:")
	except getopt.GetoptError as err:
		# print help information and exit:
		print str(err) # will print something like "option -a not recognized"
		sys.exit(2)
	for o, a in opts:
		#print(o)
		#print(a)
		if o in ("-p"):
			variable= a[0].lower()
			value=a[1:]
			setPrior(variable, value,network)
			
			#Done
		elif o in ("-m"):
			if(a[0]=='~'):
				print(marginalInverse(a[1].lower(),network))
			else:
				print marginal(a.lower(),network)
		elif o in ("-g"):
				print conditional(a[0],a[1],network)
		elif o in ("-j"):
			print "flag", o
			print "args", a 
		else:
			assert False, "unhandled option"
		

if __name__ == '__main__':
	main()


#Tests:-m~C tells us that 98.8 percent of time no cancer.
#Only marginal and set prior working.
