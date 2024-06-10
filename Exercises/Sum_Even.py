#  Write a program that calculates the sum of all the even numbers from 1 to X, where X is a user input and by using range function.

target = int(input()) # Enter a number between 0 and 1000

sum = 0
for i in range(2,target+1,2) :
  sum += i
print(sum)