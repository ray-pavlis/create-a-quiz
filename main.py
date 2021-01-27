# Quiz

#Variables
total = 0

#Start Quiz
print("Welcome to the quiz. Please answer numerically.")
print("Good luck! :)")

print("...")

#Question 1
print("Question 1: What is the capital city of Canada?")
print("1. Ottawa")
print("2. Edmonton")
print("3. Montreal")
selection1 = input("Please input your answer. ")

if (selection1 == "1"):
  print("CORRECT! :)")
  total += 1
else:
  print("Sorry, that's wrong :(")
#end if statement

print("...")

#Question 2
print("Question 2: What is Canada's national animal?")
print("1. Canadian Goose")
print("2. Loon")
print("3. Beaver")
selection2 = input("Please input your answer. ")

if (selection2 == "3"):
  print("THAT'S RIGHT! :)")
  total += 1
else:
  print("No, that's not it. :(")
#end if statement

print("...")

#Question 3
print("Question 3: What animal is on the toonie?")
print("1. Beaver")
print("2. Polar Bear")
print("3. Arctic Fox")
selection3 = input("Please input your answer. ")

if (selection3 == "2"):
  print("GOOD JOB! :)")
  total += 1
else:
  print("That isn't right. :(")
#end if statement

print("...")

#Question 4
print("Question 4: What color is the Canadian five dollar bill?")
print("1. Blue")
print("2. Purple")
print("3. Green")
selection3 = input("Please input your answer. ")

if (selection3 == "1"):
  print("YAY! YOU GOT IT RIGHT! :)")
  total += 1
else:
  print("Nope. It's not that one. :(")
#end if statement

print("...")

#Calculate percentage
percentage = 0
if (total == 0):
  percentage = 0
elif (total == 1):
  percentage = 25;
elif (total == 2):
  percentage = 50
elif (total == 3):
  percentage = 75
elif (total == 4):
  percentage = 100
#end if statement

#Print results
print("Your results are " + str(total) + "/4. That's " + str(percentage) + "%")

#Grade comments
if (total == 0):
  print("You didn't even get one right... :(")
elif (total == 1):
  print("I guess that's okay... :/")
elif (total == 2):
  print("Half right. :|")
elif (total == 3):
  print("You only got one wrong. That's pretty good. :]")
elif (total == 4):
  print("Wow! You got everything right! Awesome! :)")
#end if statement