setQ=[]
setF=[]
setSigma=[]
setGamma=[]
theStack=[]
normalDeltaTable=[]
lambdaDeltaTable=[]
inputString=""

INITIALSTATE=0
QVAL=2
F="1"
SIGMA="a,b,c,d"
GAMMA="0,1,2,3"

def qToSet():
	for i in range(QVAL):
		setQ.append(i)

def fToSet():
	for i in range(len(F)):
		if(F[i]!=","):
			setF.append(int(F[i]))

def sigmaToSet():
	for i in range(len(SIGMA)):
		if(SIGMA[i]!=","):
			setSigma.append(SIGMA[i])
			
def gammaToSet():
	for i in range(len(GAMMA)):
		if(GAMMA[i]!=","):
			setGamma.append(GAMMA[i])
	theStack.append(setGamma[0])

def createNormalTransition(input):
	#currentState, nextCharacter, topOfStack, nextState, pushToStack
	transition=[]
	currentState=-1
	nextCharacter=''
	topOfStack=''
	nextState=-1
	pushToStack=''
	
	parsedString=input.split(" ")
	currentState=int(parsedString[0])
	nextCharacter=parsedString[1]
	topOfStack=parsedString[2]
	nextState=int(parsedString[3])
	try:
		pushToStack=parsedString[4]
	except:
		pushToStack=''
	transition.append(currentState)
	transition.append(nextCharacter)
	transition.append(topOfStack)
	transition.append(nextState)
	transition.append(pushToStack)
	
	return transition

def createLambdaTransition(input):
	#lambda, currentState, topOfStack, nextState, pushToStack
	transition=[]
	currentState=-1
	topOfStack=''
	nextState=-1
	pushToStack=''
	
	parsedString=input.split(" ")
	currentState=int(parsedString[1])
	topOfStack=parsedString[2]
	nextState=int(parsedString[3])
	try:
		pushToStack=parsedString[4]
	except:
		pushToStack=''
	transition.append('L')
	transition.append(currentState)
	transition.append(topOfStack)
	transition.append(nextState)
	transition.append(pushToStack)
	
	return transition
			
def setQFSG():
	qToSet()
	fToSet()
	sigmaToSet()
	gammaToSet()



setQFSG()

t1="0 a 0 1 10"
t2="1 a 1 1 11"
t3="1 b 1 2"
t4="2 b 1 2"
t5="L 2 0 0"
	
normalDeltaTable.append(createNormalTransition(t1))
normalDeltaTable.append(createNormalTransition(t2))
normalDeltaTable.append(createNormalTransition(t3))
normalDeltaTable.append(createNormalTransition(t4))
lambdaDeltaTable.append(createLambdaTransition(t5))