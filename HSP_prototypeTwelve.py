import random
import csv

#variable initiation 
OverallScore = 0 


Q1Score = 0
Q2Score = 0
Q3Score = 0
Q4Score = 0
Q5Score = 0
Q6Score = 0

QuestionNumbers = [1,2,3,4,5,6]

name = input("please enter your name: ")
Stclass = input("please enter your class: ")

while len(QuestionNumbers) > 0:
    RandomPick = random.choice(QuestionNumbers)

    if RandomPick == 1:
        print ("""fergs owns a desktop computer with a 2.2 GHz quad-core CPU.
        He uses it to play video games and edit photographs he takes on his digital camera.""")
        responce = input("State the purpose of the CPU in the computer system? [1 mark]: ") #convert to lower case 
        answerOne = "processes data and instructions"
        answerTwo = "fetches, decodes and executes program instructions"#array of just keywords?
        if answerOne in responce:
            Q1Score += 1
        elif answerTwo in responce:
            Q1Score += 1
        else :
            print("the answer we were looking for was: ",answerOne, " or ", answerTwo)
        OverallScore += Q1Score
        print("score: ", OverallScore)
        index = QuestionNumbers.index(RandomPick)
        QuestionNumbers.pop(index)
    elif RandomPick == 2:
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
            Q2Score += 1
            if purMDR == purpose:
                Q2Score += 1
        elif register in regPC:
            Q2Score += 1
            if purPC in purpose:
                Q2Score += 1
        elif register in regAcc:
            Q2Score += 1
            if purAcc == purpose:
                Q2Score += 1
        else:
            print("the answer we were looking for was: ", regMDR, " and ", purMDR)
            print("or: ", regPC, " and ", purPC)
            print("or: ", regAcc, " and ", purAcc)
        OverallScore += Q2Score
        print("score: ", OverallScore)
        index = QuestionNumbers.index(RandomPick)
        QuestionNumbers.pop(index)
    elif RandomPick == 3:
        print("""Fergus decides to purchase a new CPU with a higher clock speed compared to the one he currently owns.
        Explain, with references to how Fergus uses his computer, the effect this will have on the computer's performance. [2 marks] """)
        responceone = input("explain: ")
        responcetwo = input("reference: ")
        answerOne = "execute more instructions per second"
        reasons = ["video games run smoother", "editing software may run faster"]
        if answerOne in responceone:
            Q3Score += 1
            if responcetwo in reasons:
                Q3Score += 1
        else:
            print("the answer we were looking for was: ", answerOne, " and ", reasons)
        OverallScore += Q3Score    
        print("score: ",OverallScore)
        index = QuestionNumbers.index(RandomPick)
        QuestionNumbers.pop(index)
    elif RandomPick == 4:
        print("Fergus' computer has 8 GB of RAM. ")
        Q4Input = input("State the purpose of RAM. [1 mark]: ")
        reasons = ["RAM stores data","RAM stores instructions","RAM stores software","RAM stores files"]
        if Q4Input in reasons:
            Q4Score += 1
        else:
            print("the answer we were looking for was: ", reasons)
        OverallScore += Q4Score    
        print("score: ",OverallScore)
        index = QuestionNumbers.index(RandomPick)
        QuestionNumbers.pop(index)
    elif RandomPick == 5:
        print("Explain what is meant by 'virtual memory' and why it may be needed by computer system.[2 marks]: ")
        responce = input("explain: ")
        partone = "allocation of secondary storage to be used like RAM"
        parttwo = "It is needed to allow the computer to open additional files when RAM is full"
        if partone in responce:
            Q5Score += 1
        if parttwo in responce:
            Q5Score += 1
        else:
            print("the answer we were looking for was: ", partone, " and ", parttwo)
        OverallScore += Q5Score    
        print("score: ",OverallScore)
        index = QuestionNumbers.index(RandomPick)
        QuestionNumbers.pop(index)
    elif RandomPick == 6:
        print ("Fergus's digital camera is an example of an 'embedded system'.")
        define = input("Define the term 'embedded system'. [1 mark]: ")
        print("Other than digital cameras, give three examples of embedded systems. [3 marks]")
        exampleOne = input("example one: ")
        exampleTwo = input("example two: ")
        exampleThree = input("example Three: ")
        partone = "Embedded systems are computers that are built into a larger system"
        examples = ["dishwasher", "television", "washing machine", "sat nav", "fitness tracker", "digital watch"]
        if partone in define:
            Q6Score += 1
        else:
            print("the answer we were looking for was: ", partone)
        if exampleOne in examples:
            Q6Score += 1
            examples.remove(exampleOne)
            
        if exampleTwo in examples:
            Q6Score += 1
            examples.remove(exampleTwo)
            
        if exampleThree in examples:
            Q6Score += 1
            examples.remove(exampleThree)
        OverallScore += Q6Score    
        print("score: ",OverallScore)
        index = QuestionNumbers.index(RandomPick)
        QuestionNumbers.pop(index)
print("final score: ", OverallScore)
with open('OutputFile.csv',mode = 'a') as OutputFile:
    OutputFileWriter = csv.writer(OutputFile, delimiter= ',', quotechar='"', quoting= csv.QUOTE_MINIMAL)
    OutputFileWriter.writerow([name, Stclass, OverallScore, Q1Score, Q2Score, Q3Score, Q4Score, Q5Score, Q6Score])
