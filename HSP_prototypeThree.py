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
    
     
