questions = (
    "Which planet is known as the 'Red Planet'?",
    "What is the process by which plants make their food called?",
    "Who wrote the play 'Hamlet'?",
    "How many sides does a hexagon have?",
    "Which of the following is a prime number?")

options=(("A. Earth", "B. Mars", "C. Jupiter", "D. Venus"),
    ("A. Respiration", "B. Photosynthesis", "C. Digestion", "D. Fermentation"),
    ("A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain"),
    ("A. Five", "B. Six", "C. Seven", "D. Eight"),
    ("A. 4", "B. 6", "C. 9", "D. 7"))

answers=("B","B","C","B","D")
guesses=[]
score=0
question_num=0
for question in questions:
    print("-------------question------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("enter your ans(A,B,C,D)").upper()
    guesses.append(guess)    
    if guess==answers[question_num]:
        score +=1
        print("correct")
    else:
        print("incorrect!")
        print(f"your correct ans is: {answers[question_num]}")    
    question_num +=1

print("------result------")
print("answer:" ,end=" ")
for answer in answers:
    print(answer,end=" ")
print()   
print("guesses:" ,end=" ")
for guess in guesses:
    print(guess,end=" ")
print()   
score=(score/len(questions))*100
print(f"you scored : {score}%")