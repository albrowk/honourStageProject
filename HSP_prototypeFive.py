score = 0
questionNumber = 0
TotalQuestions = 0
troubleQuestions = []
Totalquestions = 7
name = input("please enter your name: ")
Stclass = input("please enter your class: ")
questionNumber += 1

print ("question ",questionNumber," of ",Totalquestions)

print ("""fergs owns a desktop computer with a 2.2 GHz quad-core CPU.
He uses it to play video games and edit photographs he takes on his digital camera.""")
        
responce = input("State the purpose of the CPU in the computer system? [1 mark]: ")
        #convert to lower case 
answerOne = "processes data and instructions"
answerTwo = "fetches, decodes and executes program instructions"
        #array of just keywords?
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

print("""Fergus decides to purchase a new CPU with a higher clock speed compared to the one he currently owns.
Explain, with references to how Fergus uses his computer, the effect this will have on the computer's performance. [2 marks]: """)
responce = input("explain: ")
reason = input("reference: ")
answerOne = "execute more instructions per second"
reason = ["video games run smoother", " editing software may run faster"]

if answerOne in responce :
    score += 1
    if reason in responce:
        score += 1
        print(score)
else:
    print("the answer we were looking for was: ", answerOne, " and ", reason)
    print("score: ",score)
    troubleQuestions.append(questionNumber)
    
print("Fergus' computer has 8 GB of RAM. ")
responce = input("State the purpose of RAM. [1 mark]; ")
answer = "RAM stores"
reason = ["data","instructions","software","files"]
if answer in responce:
    if reason in responce:
        score += 1
        print(score)
else:
    print("the answer we were looking for was: ", answer, " and ", reason)
    print("score: ",score)
    troubleQuestions.append(questionNumber)
