"""
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.
"""

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

n = name1 + name2
low = n.lower()
t = low.count("t")
r = low.count("r")
u = low.count("u")
e = low.count("e")

num1 = t+r+u+e

l = low.count("l")
o = low.count("o")
v = low.count("v")
e = low.count("e")

num2 = l+o+v+e
sc = str(num1) + str(num2)
score = int(sc)
if score < 10 or score > 90 :
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50 :
  print(f"Your score is {score}, you are alright together.")
else :
  print(f"Your score is {score}.")