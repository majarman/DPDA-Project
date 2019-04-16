import os

setQ=[]
setF=[]
setSigma=[]
setGamma=[]
setDelta=[]
theStack=[]
normalDeltaTable=[]
lambdaDeltaTable=[]
inputString=""
tookLambda=False
noTransitionError=False

INITIALSTATE=0
currentState=INITIALSTATE

QVAL=""
F=""
SIGMA=""
GAMMA=""
DELTA=""

#__ToSet:
#individual functions for populating setQ, setF, setSigma, setGamma
def qToSet():
	for i in range(int(QVAL)+1):
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

#the machine. This gets passed a string and determines if the string is in the language
def isStringInLanguage(string):
	#initializing variables here
	machineStatus=[]
	nextMove=[]
	global INITIALSTATE
	global currentState
	currentState=INITIALSTATE
	global theStack
	theStack=[]
	theStack.append(setGamma[0])
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

#validation method for the machine
#returns 1 if machine is a DPDA, 0 if not
def validate():
	#checks normalDeltaTable for states or symbols not in the defined sets Q, F, Sigma, and Gamma
	for i in range(len(normalDeltaTable)):
		if(normalDeltaTable[i][0] not in setQ):
			print("Error: normalDeltaTable contains invalid state")
			return 0
		if(normalDeltaTable[i][1] not in setSigma):
			print("Error: normalDeltaTable contains invalid alphabet symbol")
			return 0
		if(normalDeltaTable[i][2] not in setGamma):
			print("Error: normalDeltaTable contains invalid stack symbol")
			return 0
		if(normalDeltaTable[i][3] not in setQ):
			print("Error: normalDeltaTable contains invalid state")
			return 0
		if(normalDeltaTable[i][4] != ''):
			for x in range(len(normalDeltaTable[i][4])):
				if(normalDeltaTable[i][4][x] not in setGamma):
					print("Error: normalDeltaTable contains invalid stack symbol")
					return 0
	#checks lambdaDeltaTable for states or symbols not in the defined sets Q, F, Sigma, and Gamma
	for i in range(len(lambdaDeltaTable)):
		if(lambdaDeltaTable[i][1] not in setQ):
			print("Error: lambdaDeltaTable contains invalid state")
			return 0
		if(lambdaDeltaTable[i][2] not in setGamma):
			print("Error: lambdaDeltaTable contains invalid stack symbol")
			return 0
		if(lambdaDeltaTable[i][3] not in setQ):
			print("Error: lambdaDeltaTable contains invalid state")
			return 0
		if((lambdaDeltaTable[i][4] != '') and (lambdaDeltaTable[i][4] not in setGamma)):
			print("Error: lambdaDeltaTable contains invalid stack symbol")
			return 0
	#checks setF for states not in set Q
	for i in range(len(setF)):
		if(setF[i] not in setQ):
			print("Error: setF contains invalid state not found in setQ")
			return 0
	return 1
	
#main method that runs the program
def main():
	global QVAL
	global F
	global SIGMA
	global GAMMA
	global DELTA
	goAgain=True
	
	#initializes PATH for files
	PATH=os.path.dirname(os.path.abspath("main.py"))
	print(PATH)
	s=input("Use current directory? (enter 'yes' or 'no')\n")
	if(s=='no'):
		PATH=input("Specify path: ")
	#opens files
	try:
		qFile=open((PATH+"\Q.conf"), "r")
		fFile=open((PATH+"\F.conf"), "r")
		sFile=open((PATH+"\Sigma.conf"), "r")
		gFile=open((PATH+"\Gamma.conf"), "r")
		dFile=open((PATH+"\delta.conf"), "r")
	except:
		print("Problem opening file.")
	
	#takes in complete files as strings and assigns those strings to the main variables
	QVAL=qFile.read()
	F=fFile.read()
	SIGMA=sFile.read()
	GAMMA=gFile.read()
	DELTA=dFile.read()
	
	#configures the machine by calling methods that create the list objects
	try:
		setQFSG()
		setDelta=DELTA.splitlines()
		createTransitions(setDelta)
	except:
		print("Error configuring machine. Check formatting guidelines in the README")
		return
	
	print("Machine configured. Validating...")
	
	#validates the machine
	if(validate()==1):
		print("Machine passes validation.")
	elif(validate()==0):
		print("Machine does not pass validation. See error above.")
		return -1
	
	print("Machine initialized.")
	
	print("q: ")
	print(setQ)
	print("F: ")
	print(setF)
	print("Sigma: ")
	print(setSigma)
	print("Gamma: ")
	print(setGamma)
	print("Delta: ")
	print(setDelta)
	print("\n")
	
	#main machine loop
	while(goAgain):
		s=input("Enter string: ")
		#checks if string contains invalid symbols not in setSigma
		validString=True
		for i in range(len(s)):
			if(s[i] not in setSigma):
				print("Error: string invalid (contains symbols not in setSigma)")
				validString=False
				break
		if(validString):
			isStringInLanguage(s)
		
		s=input("Enter another string? (enter 'yes' or 'no')\n")
		if(s=="yes"):
			goAgain=True
		elif(s=="no"):
			goAgain=False

main()