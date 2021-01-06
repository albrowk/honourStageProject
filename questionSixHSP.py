
#question 6
#questionNumber += 1
score = 0
#print ("question ",questionNumber," of ",Totalquestions)
print ("Fergus's digital camera is an example of an 'embedded system'.")
define = input("Define the term 'embedded system'. [1 mark]: ")
example = input("Other than digital cameras, give three examples of embedded systems. [3 marks]: ")
partone = "Embedded systems are computers that are built into a larger system"
examples = ["dishwasher", "television", "washing machine", "sat nav", "fitness tracker", "digital watch"]
if partone in define:
    score += 1
else:
    print("the answer we were looking for was: ", partone)

scores = 0
while scores > 3:
    for i in examples:
        if example in examples:
            print("yes")
            score += 1
            scores += 1
        else:
            print("the answer we were looking for was: ",examples)
            print("score: ", score)
            #troubleQuestions.append(questionNumber)
print(score)
