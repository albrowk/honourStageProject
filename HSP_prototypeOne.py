name = ""
Stclass = ""
score = 0
questionNumber = 0
responce = ""
answer = ""
TotalQuestions = 0
troubleQuestions = []
Totalquestions = 2
name = input("please enter your name: ")
print(name)
Stclass = input("please enter your class: ")
print(Stclass)
questionNumber += 1
print ("question ",questionNumber," of ",Totalquestions)
responce = input("what does CPU stand for? ")
answer = "central processing unit"
#responce = responce.lower()
if responce == answer:
    score += 1
    print("score: ",score)
else:
    print("the answer we were looking for was: ",answer)
    print("score: ",score)
    troubleQuestions.append(questionNumber)
    print(troubleQuestions)
