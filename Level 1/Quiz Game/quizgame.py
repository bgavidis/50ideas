q1 = input("What is the capital of France?")
q2 = input("What is the capital of Spain?")
q3 = input("What is the capital of Germany?")
q4 = input("What is the capital of Italy?")
q5 = input("What is the capital of India?")
score = 0
if q1 == "Paris":
    score += 1
if q2 == "Madrid":
    score += 1
if q3 == "Berlin":
    score += 1
if q4 == "Rome":
    score += 1
if q5 == "New Delhi":
    score += 1

print("Your score is: "+ str(score),"/ 5")