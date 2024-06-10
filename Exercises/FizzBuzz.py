"""
Write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

    -> Include number 100.
    -> If number divisible by 3 then, print "Fizz".
    -> If number divisible by 5, then print "Buzz".`
    -> If number divisible by both 3 and 5, then print "FizzBuzz"
"""

for i in range(1,101) :
  if i % 3 == 0 and i % 5 == 0 :
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)