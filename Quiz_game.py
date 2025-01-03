print ("Welcome to this quiz game!")
print ("Do you want to play this game? ")
answer = input("Yes/No: ")
if answer.lower() != "yes":
  print ("Goodbye!")
  quit()
else :
  print ("Let's begin! \n")

score = 0;

# Question 1

print ("Question 1: Which famous inventor created the light bulb?")
print ("a) Nikola Tesla")
print ("b) Thomas Edison")
print ("c) Albert Einstein")
print ("d) William Shakespeare")

answer = input("Enter one of the following: a,b,c,d \n ") 

if answer.lower() == "b":
  score += 1
  print ("Correct! \n")
else :
  print ("Incorrect!")
  print ("The correct answer is b) Thomas Edison \n")

# Question 2

print ("Question 2: Who invented the telephone?")
print ("a) Thomas Edison")
print ("b) Nikola Tesla")
print ("c) Albert Einstein")
print ("d) William Shakespeare")

answer = input("Enter one of the following: a,b,c,d \n")

if answer.lower() == "a":
  score += 1
  print ("Correct! \n")

else :
  print ("Incorrect!")
  print ("The correct answer is a) Thomas Edison \n")

# Question 3

print ("Question 3: Who is credited with inventing the modern television?")
print ("a) Nikola Tesla")
print ("b) Thomas Edison")
print ("c) Albert Einstein")
print ("d) William Shakespeare")

answer = input("Enter one of the following: a,b,c,d \n")

if answer.lower() == "c":
  score += 1
  print ("Correct! \n")

else :
  print ("Incorrect!")
  print ("The correct answer is c) Albert Einstein \n")

# Question 4

print ("Question 4: Who is credited with inventing the light bulb?")
print ("a) Nikola Tesla")
print ("b) Thomas Edison")
print ("c) Albert Einstein")
print ("d) William Shakespeare")

answer = input("Enter one of the following: a,b,c,d \n")

if answer.lower() == "b":
  score += 1
  print ("Correct! \n")

else :
  print ("Incorrect!")
  print ("The correct answer is b) Thomas Edison \n")

# Question 5

print ("Question 5: Who is credited with inventing the modern airplane?")
print ("a) Nikola Tesla")
print ("b) Thomas Edison")
print ("c) Albert Einstein")
print ("d) William Shakespeare")

answer = input("Enter one of the following: a,b,c,d \n")

if answer.lower() == "a":
  score += 1
  print ("Correct! \n")

else :
  print ("Incorrect!")
  print ("The correct answer is a) Nikola Tesla \n")

# Question 6
print("Question 6: What is the capital city of France?")
print("a) Madrid")
print("b) Berlin")
print("c) Paris")
print("d) Rome")

answer = input("Enter one of the following: a,b,c,d \n")

if answer.lower() == "c":
  score += 1
  print ("Correct! \n")

else :
  print ("Incorrect!")
  print ("The correct answer is c) Paris \n")

# Question 7
print("Question 7: Which planet is known as the Red Planet?")
print("a) Venus")
print("b) Mars")
print("c) Jupiter")
print("d) Saturn")

answer = input("Enter one of the following: a,b,c,d \n")

if answer.lower() == "b":
  score += 1
  print ("Correct! \n")

else :
  print ("Incorrect!")
  print ("The correct answer is b) Mars \n")

# Question 8
print("Question 8: Who painted the Mona Lisa?")
print("a) Vincent van Gogh")
print("b) Pablo Picasso")
print("c) Leonardo da Vinci")
print("d) Claude Monet")

answer = input("Enter one of the following: a,b,c,d \n")

if answer.lower() == "a":
  score += 1
  print ("Correct! \n")

else :
  print ("Incorrect!")
  print ("The correct answer is a) Vincent van Gogh \n")

# Question 9
print("Question 9: What is the largest mammal in the world?")
print("a) African Elephant")
print("b) Blue Whale")
print("c) Giraffe")
print("d) Polar Bear")

answer = input("Enter one of the following: a,b,c,d \n")

if answer.lower() == "a":
  score += 1
  print ("Correct! \n")

else :
  print ("Incorrect!")
  print ("The correct answer is a) African Elephant \n")

# Question 10
print("Question 10: Who wrote 'Romeo and Juliet'?")
print("a) William Shakespeare")
print("b) Charles Dickens")
print("c) Jane Austen")
print("d) Mark Twain")

answer = input("Enter one of the following: a,b,c,d \n")

if answer.lower() == "c":
  score += 1
  print ("Correct! \n")

else :
  print ("Incorrect!")
  print ("The correct answer is c) Jane Austen \n")

print ("Your final score is: ", score)
print ("Thank you for playing! Goodbye!")