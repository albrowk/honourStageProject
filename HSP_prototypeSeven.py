score = 0
questionNumber = 0
TotalQuestions = 0
troubleQuestions = []
Totalquestions = 6
name = input("please enter your name: ")
Stclass = input("please enter your class: ")

#question 1
questionNumber += 1
print ("question ",questionNumber," of ",Totalquestions)
print ("""fergs owns a desktop computer with a 2.2 GHz quad-core CPU.
He uses it to play video games and edit photographs he takes on his digital camera.""")
responce = input("State the purpose of the CPU in the computer system? [1 mark]: ") #convert to lower case 
answerOne = "processes data and instructions"
answerTwo = "fetches, decodes and executes program instructions"#array of just keywords?
if answerOne in responce:
    score += 1
    print("score: ",score)
elif answerTwo in responce:
    score += 1
    print("score: ",score)
else :
    print("the answer we were looking for was: ",answerOne, " or ", answerTwo)
    print("score: ",score)
    troubleQuestions.append(questionNumber)
    
#question 2
questionNumber += 1    
print ("question ",questionNumber," of ",Totalquestions)
print("""Fergus' CPU uses Von Neumann architecture and features various registers.
One of these registers is the MAR ( memory address register).
State one other register used in Von Neumann architecture and the purpose of the register.  [2 marks]: """)
register = input("Register: ")
purpose = input("Purpose: ")
regMDR = ["memory data register", "MDR"]
regPC = ["program counter", "PC"]
regAcc = ["accumulator"]
purMDR = "holds data waiting to be processed"
purPC = "points to next instructions"
purAcc = "strore result of calculation"
if register in regMDR:
    score += 1
    if purMDR == purpose:
        score += 1
        print("score: ",score)
elif register in regPC:
    score += 1
    if purPC in purpose:
        score += 1
        print("score: ",score)
elif register in regAcc:
    score += 1
    if purAcc == purpose:
        score += 1
        print("score: ",score)
else:
    print("the answer we were looking for was: ", regMDR, " and ", purMDR)
    print("or: ", regPC, " and ", purPC)
    print("or: ", regAcc, " and ", purAcc)
    print("score: ",score)
    troubleQuestions.append(questionNumber)

#question 3
questionNumber += 1
print ("question ",questionNumber," of ",Totalquestions)
print("""Fergus decides to purchase a new CPU with a higher clock speed compared to the one he currently owns.
Explain, with references to how Fergus uses his computer, the effect this will have on the computer's performance. [2 marks] """)
responceone = input("explain: ")
responcetwo = input("reference: ")
answerOne = "execute more instructions per second"
reasons = ["video games run smoother", "editing software may run faster"]
if answerOne in responceone:
    score += 1
    if responcetwo in reasons:
        score += 1
        print(score)
else:
    print("the answer we were looking for was: ", answerOne, " and ", reasons)
    print("score: ",score)
    troubleQuestions.append(questionNumber)

#question 4
questionNumber += 1
print("Fergus' computer has 8 GB of RAM. ")
Q4Input = input("State the purpose of RAM. [1 mark]: ")
reasons = ["RAM stores data","RAM stores instructions","RAM stores software","RAM stores files"]
if Q4Input in reasons:
    score += 1
    print("score: ", score)
else:
    print("the answer we were looking for was: ", reasons)
    print("score: ",score)
    troubleQuestions.append(questionNumber)

#question 5  
questionNumber += 1
print ("question ",questionNumber," of ",Totalquestions)
print("Explain what is meant by 'virtual memory' and why it may be needed by computer system.[2 marks]: ")
responce = input("explain: ")
partone = "allocation of secondary storage to be used like RAM"
parttwo = "It is needed to allow the computer to open additional files when RAM is full"
if partone in responce:
    score += 1
if parttwo in responce:
    score += 1
    print(score)
else:
    print("the answer we were looking for was: ", partone, " and ", parttwo)
    print("score: ",score)
    troubleQuestions.append(questionNumber)
    
#question 6
questionNumber += 1
print ("question ",questionNumber," of ",Totalquestions)
print ("Fergus's digital camera is an example of an 'embedded system'.")
define = input("Define the term 'embedded system'. [1 mark]: ")
print("Other than digital cameras, give three examples of embedded systems. [3 marks]")
exampleOne = input("example one: ")
exampleTwo = input("example two: ")
exampleThree = input("example Three: ")
partone = "Embedded systems are computers that are built into a larger system"
examples = ["dishwasher", "television", "washing machine", "sat nav", "fitness tracker", "digital watch"]
if partone in define:
    score += 1
else:
    print("the answer we were looking for was: ", partone)
    
if exampleOne in examples:
    score += 1
    examples.remove(exampleOne)
    
if exampleTwo in examples:
    score += 1
    examples.remove(exampleTwo)
    
if exampleThree in examples:
    score += 1
    examples.remove(exampleThree)
troubleQuestions.append(questionNumber)

print(score)
print(troubleQuestions)
