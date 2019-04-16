setQ=[]
setF=[]
setSigma=[]
setGamma=[]
theStack=[]
setDelta=[]
normalDeltaTable=[]
lambdaDeltaTable=[]
inputString=""
tookLambda=False
noTransitionError=False

INITIALSTATE=0
currentState=INITIALSTATE

QVAL=2
F="0"
SIGMA="ab"
GAMMA="01"
DELTA="""0 a 0 1 10
1 a 1 1 11
1 b 1 2
2 b 1 2
L 2 0 0"""

#__ToSet:
#individual functions for populating setQ, setF, setSigma, setGamma
def qToSet():
	for i in range(QVAL):
		setQ.append(i)

def fToSet():
	for i in range(len(F)):
		if(F[i]!=","):
			setF.append(int(F[i]))

def sigmaToSet():
	for i in range(len(SIGMA)):
		setSigma.append(SIGMA[i])
			
def gammaToSet():
	for i in range(len(GAMMA)):
		setGamma.append(GAMMA[i])
	theStack.append(setGamma[0])

#initializes and populates setQ, setF, setSigma, setGamma	
def setQFSG():
	qToSet()
	fToSet()
	sigmaToSet()
	gammaToSet()

#string input
#returns 5-tuple array representing a transition
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

#string input
#returns 5-tuple array representing a transition
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

#5-tuple setD
#populates transition tables
def createTransitions(setD):
	for i in range(len(setD)):
		if (setD[i][0]=='L'):
			lambdaDeltaTable.append(createLambdaTransition(setD[i]))
		else:
			normalDeltaTable.append(createNormalTransition(setD[i]))

#char char
#returns 3-tuple representing the current state
def getMachineStatus(char=''):
	state=[]
	state.append(currentState)
	state.append(char)
	print("stack:")
	print(theStack)
	try:
		state.append(theStack.pop())
		theStack.append(state[2])
	except IndexError:
		state.append('')
	return state

#3-tuple state
#returns 2-tuple representing next state and symbols to push to the stack, or None if no matching transitions found
def getNextMove(state):
	nextState=-1
	pushToStack=""
	global tookLambda
	tookLambda=False
	global noTransitionError
	for i in range(len(normalDeltaTable)):
		if ((normalDeltaTable[i][0]==state[0]) and ((normalDeltaTable[i][1]==state[1]) and (normalDeltaTable[i][2]==state[2]))):
			nextState=normalDeltaTable[i][3]
			pushToStack=normalDeltaTable[i][4]
			return [nextState, pushToStack]
	
	print("No normal transitions found. Searching lambda transitions...\n")
	
	for i in range(len(lambdaDeltaTable)):
		if ((lambdaDeltaTable[i][1]==state[0]) and (lambdaDeltaTable[i][2]==state[2])):
			nextState=lambdaDeltaTable[i][3]
			pushToStack=lambdaDeltaTable[i][4]
			tookLambda=True
			return [nextState, pushToStack]

	print("no transition found!\n")
	noTransitionError=True

#main function gets passed a string and determines if the string is in the language
def isStringInLanguage(string):
	machineStatus=[]
	nextMove=[]
	global currentState
	global theStack
	global noTransitionError
	noTransitionError=False
	i=0
	#main loop
	while (i < len(string)):
		print("\nSTEP: "+str(i))
		machineStatus=getMachineStatus(string[i])
		print("Machine Status: ")
		print(machineStatus)
		#get nextMove from the transition table
		nextMove=getNextMove(machineStatus)
		print("Matching transition: ")
		print(nextMove)
		#make the move
		try:
			currentState=nextMove[0]
			print("New State: ")
			print(currentState)
			theStack.pop()
			theStack.append(nextMove[1][1])
			theStack.append(nextMove[1][0])
			print("Stack after push: ")
			print(theStack)
		#if just pop and no push
		except IndexError:
			currentState=nextMove[0]
			print("Stack after pop: ")
			print(theStack)
		#happens if getNextMove returned nothing bc noTransitionError
		except:
			print("\nException occurred (noTransitionError)\n")
			print("machineStatus: ")
			print(machineStatus)
			print("nextMove: ")
			print(nextMove)
			break
		#if you took a lambda transition, don't skip the next char
		if(tookLambda):
			i-=1
		#increment
		i+=1
	#reject if noTransitionError
	if(noTransitionError):
		print("\nString rejected!")
		return
	
	#check to see if after string read, in final state
	elif (currentState in setF):
		print("\nString accepted!")
		return
	
	#if not in final state, try one last lambda transition
	print("\nEnd of string, not in final state.\nTrying one last lambda transition...")
	#getMachineStatus passed nothing so it interprets it as lambda
	machineStatus=getMachineStatus()
	print("Machine Status: ")
	print(machineStatus)
	#get nextMove from the transition table
	nextMove=getNextMove(machineStatus)
	print("Matching transition: ")
	print(nextMove)
	#make the move
	try:
		currentState=nextMove[0]
		print("New state: ")
		print(currentState)
		theStack.pop()
		theStack.append(nextMove[1][1])
		theStack.append(nextMove[1][0])
		print("Stack after push:")
		print(theStack)
	#if just pop and no push
	except IndexError:
		currentState=nextMove[0]
		print("Stack after pop: ")
		print(theStack)
	#happens if getNextMove returned nothing bc noTransitionError
	except:
		print("\nException occurred (noTransitionError)\n")
		print("machineStatus: ")
		print(machineStatus)
		print("nextMove: ")
		print(nextMove)
	
	#reject if noTransitionError
	if(noTransitionError):
		print("\nString rejected!")
		return
	
	#check to see if after string read, in final state
	elif (currentState in setF):
		print("\nString accepted!")
		return

setQFSG()
setDelta=DELTA.splitlines()
createTransitions(setDelta)

isStringInLanguage("aaaabbbb")