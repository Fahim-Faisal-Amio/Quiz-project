print("Quiz test!")

playing = input("Do you want to start the quiz? ")

if playing.lower() != "yes":
    quit()

print("The quiz is starting :)")
score = 0

answer = input("What is meant by EPS? ")
if answer.lower() == "electrical power steering":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is meant by uj? ")
if answer.lower() == "universal joint":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is meant by sts? ")
if answer.lower() == "steering torque sensor":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is meant by sas? ")
if answer.lower() == "steering angle sensor":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Points " + str(score) + " questions correct!")
print("Points " + str((score / 4) * 100) + "%.")
